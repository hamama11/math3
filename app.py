import math
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ============================================
# 페이지 설정
# ============================================
st.set_page_config(
    page_title="🕵️ SM 수학사무소",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CSS 커스터마이징
# ============================================
st.markdown("""
    <style>
    .big-font {
        font-size: 3rem !important;
        font-weight: bold;
        text-align: center;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .success-card {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 15px;
        border-radius: 10px;
        color: #333;
    }
    .warning-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 15px;
        border-radius: 10px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# 세션 상태 초기화
# ============================================
if 'investigation_log' not in st.session_state:
    st.session_state.investigation_log = []
if 'found_answers' not in st.session_state:
    st.session_state.found_answers = {}

# ============================================
# 수학 함수들 (원본 유지)
# ============================================
def cube_root(x: float) -> float:
    return x ** (1/3)

def find_a_by_cubes(x: int):
    a = 1
    rows = []
    while True:
        left = a**3
        right = (a+1)**3
        rows.append({"a": a, "a³": left, "(a+1)³": right, "범위": f"✓" if left < x < right else ""})
        if left < x < right:
            return a, pd.DataFrame(rows)
        a += 1
        if a > 100000:
            raise ValueError("a search exceeded limit")

def find_b_by_substitution(x: int, a: int, b_max: int = 8):
    rows = []
    chosen_b = None
    for b in range(0, b_max+1):
        t = a + b/10
        val = t**3
        ok = val < x
        status = "🎯" if ok else "❌"
        rows.append({"b": b, "t": f"{t:.1f}", "t³": f"{val:.3f}", "상태": status})
        if ok:
            chosen_b = b
        else:
            break
    if chosen_b is None:
        chosen_b = 0
    L = (a + chosen_b/10)**3
    U = (a + (chosen_b+1)/10)**3
    return chosen_b, pd.DataFrame(rows), L, U

def algebraic_linear_guess_b(x: int, a: int):
    delta = x - a**3
    h = delta / (3*(a**2))
    ten_h = 10*h
    b0 = int(round(ten_h))
    return delta, h, ten_h, b0

def newton_iter(x: int, t0: float, max_iter: int = 6, tol: float = 1e-10):
    rows = []
    t = t0
    for k in range(max_iter):
        t3 = t**3
        err = t3 - x
        rows.append({"반복": k, "t": f"{t:.8f}", "t³": f"{t3:.3f}", "오차": f"{err:.8f}"})
        if abs(err) < tol:
            break
        t = t + (x - t3) / (3*(t**2))
    t3 = t**3
    err = t3 - x
    rows.append({"반복": k+1, "t": f"{t:.8f}", "t³": f"{t3:.3f}", "오차": f"{err:.8f}"})
    return t, pd.DataFrame(rows)

# ============================================
# 헤더
# ============================================
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.write("## 🕵️")

with col2:
    st.markdown("""
    # 🔍 SM 수학사무소
    ### 세제곱근 비밀번호 추적 미션
    """)

with col3:
    st.write("## 📊")

st.markdown("---")

# ============================================
# 사이드바
# ============================================
with st.sidebar:
    st.markdown("## 🎮 제어판")
    
    # 난이도 선택
    difficulty = st.radio(
        "📈 난이도 선택",
        ["🟢 초급 (2-10)", "🟡 중급 (10-100)", "🔴 상급 (100-1000)"]
    )
    
    # 범위 설정
    if "초급" in difficulty:
        x_range = (2, 10)
    elif "중급" in difficulty:
        x_range = (10, 100)
    else:
        x_range = (100, 1000)
    
    st.divider()
    
    x = st.number_input(
        "🎯 추적 대상 숫자 (x)",
        min_value=x_range[0],
        max_value=x_range[1],
        value=15,
        step=1
    )
    
    st.divider()
    
    st.markdown("### ⚙️ 뉴턴 근사 설정")
    max_iter = st.slider("반복 횟수", 1, 12, 6)
    tol_pow = st.select_slider(
        "정밀도 (오차 한계)",
        [-2, -4, -6, -8, -10, -12],
        value=-10
    )
    tol = 10.0**tol_pow
    
    use_custom_t0 = st.checkbox("🔧 초기값 직접 설정")
    if use_custom_t0:
        t0_custom = st.number_input("t₀ 값", value=3.0, step=0.1)
    else:
        t0_custom = None
    
    st.divider()
    
    # 통계
    st.markdown("### 📈 통계")
    if st.session_state.found_answers:
        st.metric("✅ 해결한 미션", len(st.session_state.found_answers))

# ============================================
# 메인 콘텐츠
# ============================================

# 1. 목표 설정
st.markdown("## 🎪 미션 브리핑")

# 대상값 표시
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card"><h2>🎯 대상값</h2><p style="font-size:2rem">x = ' + str(int(x)) + '</p></div>', unsafe_allow_html=True)

with col2:
    true_root = cube_root(float(x))
    st.markdown(f'<div class="metric-card"><h2>🎁 정답</h2><p style="font-size:2rem">∛x ≈ {true_root:.4f}</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="metric-card"><h2>🔍 소수점 첫자리</h2><p style="font-size:2rem">{str(true_root)[2]}</p></div>', unsafe_allow_html=True)

st.markdown("---")

# 2. 인터랙티브 레이더 (범위 찾기)
st.markdown("## 📡 정수 범위 탐지 레이더")

a, df_a = find_a_by_cubes(int(x))

# 진행률 계산
progress = (x - a**3) / ((a+1)**3 - a**3)
progress = max(0, min(1, progress))

col1, col2 = st.columns([3, 1])
with col1:
    st.progress(progress, text=f"범위: {a}³ < {x} < {a+1}³")
with col2:
    st.metric("정수 부분", a)

# 상세 테이블
with st.expander("🔍 정수 탐색 상세 로그"):
    st.dataframe(df_a, use_container_width=True, hide_index=True)

st.markdown("---")

# 3. 4가지 수사 방법 (탭)
st.markdown("## 🔬 4가지 수사 방법")

tab1, tab2, tab3, tab4, tab_bonus = st.tabs([
    "🎯 방법1: 대입법",
    "📈 방법2: 그래프법", 
    "📐 방법3: 대수근사법",
    "🔁 방법4: 뉴턴법",
    "🏆 보너스"
])

# ============================================
# Tab 1: 대입법 (Interactive)
# ============================================
with tab1:
    st.markdown("### 직접 대입해서 정답 찾기")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**내 추측값 입력:**")
        user_guess = st.slider(
            "b 선택 (소수 첫째 자리)",
            min_value=0,
            max_value=9,
            value=3,
            key="user_guess"
        )
        
        t_guess = a + user_guess / 10
        result_guess = t_guess ** 3
        
        st.metric(f"(a + b/10) = {a} + {user_guess}/10", f"{t_guess:.1f}")
        st.metric(f"t³ = ", f"{result_guess:.4f}")
        
        # 검증
        if result_guess < x:
            st.info(f"✓ {result_guess:.4f} < {x} (범위 내!)")
        elif result_guess > (a + (user_guess+1)/10)**3:
            st.error(f"✗ {result_guess:.4f} > {(a + (user_guess+1)/10)**3:.4f} (범위 초과)")
        else:
            st.success(f"🎯 정답 발견!")
    
    with col2:
        # 자동 방법
        b_sub, df_b, L, U = find_b_by_substitution(int(x), a, b_max=9)
        st.write("**자동 탐색 결과:**")
        st.dataframe(df_b, use_container_width=True, hide_index=True)
        st.success(f"🎯 b = {b_sub} (자동 정답)")

# ============================================
# Tab 2: 그래프법
# ============================================
with tab2:
    st.markdown("### 곡선에서 교점 찾기")
    
    # Plotly 인터랙티브 그래프
    t_min = max(0.1, a - 0.5)
    t_max = a + 1.5
    ts = np.linspace(t_min, t_max, 500)
    ys = ts**3
    
    fig = go.Figure()
    
    # 곡선
    fig.add_trace(go.Scatter(
        x=ts, y=ys,
        mode='lines',
        name='y = t³',
        line=dict(color='blue', width=3)
    ))
    
    # 목표선
    fig.add_hline(y=x, line_dash="dash", line_color="red", 
                  annotation_text=f"y = {x}")
    
    # 격자선 (0.1 간격)
    for k in range(0, 15):
        fig.add_vline(x=a + k/10, line_dash="dot", line_color="gray", 
                      opacity=0.3)
    
    # 정답점
    fig.add_trace(go.Scatter(
        x=[true_root], y=[x],
        mode='markers',
        name='정답',
        marker=dict(size=15, color='green', symbol='star')
    ))
    
    fig.update_layout(
        title="y = t³ 그래프에서 교점 찾기",
        xaxis_title="t (세제곱근)",
        yaxis_title="y (세제곱값)",
        hovermode='closest',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info(f"💡 0.1 간격 격자에서 교점이 있는 구간을 찾으세요!")

# ============================================
# Tab 3: 대수근사법
# ============================================
with tab3:
    st.markdown("### 다항식 전개로 공식 유도")
    
    delta, h_lin, ten_h, b0 = algebraic_linear_guess_b(int(x), a)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📝 1단계: 기본 공식")
        st.latex(r"x = a^3 + 3a^2h + 3ah^2 + h^3")
        st.write("작은 항 무시:")
        st.latex(r"x \approx a^3 + 3a^2h")
    
    with col2:
        st.markdown("### 🧮 2단계: h 계산")
        st.latex(r"h \approx \frac{x - a^3}{3a^2}")
        st.metric("Δ = x - a³", delta)
        st.metric("h ≈", f"{h_lin:.6f}")
    
    with col3:
        st.markdown("### 🎯 3단계: b 예측")
        st.latex(r"10h \approx b")
        st.metric("10h ≈", f"{ten_h:.3f}")
        st.metric("제안 b", b0)

# ============================================
# Tab 4: 뉴턴법
# ============================================
with tab4:
    st.markdown("### 접선으로 빠르게 수렴시키기")
    
    st.latex(r"t_{n+1} = t_n + \frac{x - t_n^3}{3t_n^2}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 반복 과정")
        t0 = float(t0_custom) if t0_custom else float(a)
        t_final, df_newton = newton_iter(int(x), t0, max_iter, tol)
        st.dataframe(df_newton, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("### 수렴 시각화")
        iterations = df_newton['반복'].tolist()
        errors = [float(e) for e in df_newton['오차'].tolist()]
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.semilogy(iterations, [abs(e) for e in errors], 'bo-', linewidth=2, markersize=8)
        ax.set_xlabel('반복 횟수', fontsize=12)
        ax.set_ylabel('|오차| (로그 스케일)', fontsize=12)
        ax.set_title('뉴턴법 수렴 속도', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    
    st.success(f"🎉 최종값: t = {t_final:.10f}")

# ============================================
# Tab 보너스
# ============================================
with tab_bonus:
    st.markdown("### 🏆 보너스 챌린지")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎮 다양한 x값으로 시도")
        challenge_x = st.selectbox(
            "도전할 숫자",
            [2, 3, 5, 7, 10, 50, 100, 256, 343, 512]
        )
        
        if st.button("🚀 새 미션 시작"):
            st.session_state.found_answers[challenge_x] = True
            st.balloons()
            st.success(f"미션 #{len(st.session_state.found_answers)} 추가됨!")
    
    with col2:
        st.markdown("#### 📊 미션 통계")
        if st.session_state.found_answers:
            for num in st.session_state.found_answers:
                st.write(f"✅ x = {num}")
        else:
            st.info("아직 완료한 미션이 없습니다.")
    
    st.divider()
    
    st.markdown("#### 🧠 심화 이론")
    st.markdown("""
    **케플러의 제3법칙**: 행성의 공전주기 T와 궤도반지름 R의 관��
    - $T^2 \\propto R^3$
    - 따라서 $R \\propto \\sqrt[3]{T^2}$
    
    **3D 프린팅 스케일링**: 부피를 $V$배로 늘리려면 각 변을 $\\sqrt[3]{V}$배로
    
    **금융**: 3년간 복리 수익률 계산에도 세제곱근이 사용됩니다!
    """)

st.markdown("---")

# ============================================
# 푸터
# ============================================
st.markdown("""
    <div style="text-align: center; color: gray; font-size: 0.8rem; padding: 20px;">
    🕵️ SM 수학사무소 | 세제곱근 수사 게임 v1.0<br>
    Created with Streamlit | Math Engine Powered
    </div>
""", unsafe_allow_html=True)
