import math
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="🕵️ SM 수학사무소",
    page_icon="🔍",
    layout="wide"
)

st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# 수학 함수들
# ============================================
def cube_root(x: float) -> float:
    return x ** (1/3)

def find_a_by_cubes(x: int):
    a = 1
    rows = []
    while True:
        left = a**3
        right = (a+1)**3
        rows.append({"a": a, "a³": left, "(a+1)³": right})
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
        rows.append({"b": b, "t": f"{t:.1f}", "t³": f"{val:.3f}", "상태": "🎯" if ok else "❌"})
        if ok:
            chosen_b = b
        else:
            break
    if chosen_b is None:
        chosen_b = 0
    L = (a + chosen_b/10)**3
    U = (a + (chosen_b+1)/10)**3
    return chosen_b, pd.DataFrame(rows), L, U

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
st.markdown("# 🔍 SM 수학사무소")
st.markdown("### 세제곱근 비밀번호 추적 미션")
st.divider()

# ============================================
# 사이드바
# ============================================
with st.sidebar:
    st.markdown("## 🎮 제어판")
    
    difficulty = st.radio(
        "📈 난이도",
        ["🟢 초급 (2-10)", "🟡 중급 (10-100)", "🔴 상급 (100-1000)"]
    )
    
    if "초급" in difficulty:
        x_range = (2, 10)
    elif "중급" in difficulty:
        x_range = (10, 100)
    else:
        x_range = (100, 1000)
    
    x = st.number_input(
        "🎯 추적 대상 (x)",
        min_value=x_range[0],
        max_value=x_range[1],
        value=15,
        step=1
    )
    
    st.divider()
    max_iter = st.slider("반복 횟수", 1, 12, 6)
    tol_pow = st.select_slider("정밀도", [-2, -4, -6, -8, -10, -12], value=-10)
    tol = 10.0**tol_pow
    use_custom_t0 = st.checkbox("초기값 설정")
    t0_custom = st.number_input("t₀", value=3.0, step=0.1) if use_custom_t0 else None

# ============================================
# 메인
# ============================================
st.markdown("## 🎪 미션 브리핑")

true_root = cube_root(float(x))
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<div class="metric-card"><h3>🎯 대상값</h3><p style="font-size:2rem">x = {int(x)}</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="metric-card"><h3>🎁 정답</h3><p style="font-size:2rem">∛x ≈ {true_root:.4f}</p></div>', unsafe_allow_html=True)

with col3:
    decimal_part = str(true_root)[2] if len(str(true_root)) > 2 else "?"
    st.markdown(f'<div class="metric-card"><h3>🔍 소수점 첫자리</h3><p style="font-size:2rem">{decimal_part}</p></div>', unsafe_allow_html=True)

st.divider()

# 범위 탐지
st.markdown("## 📡 정수 범위 탐지")
a, df_a = find_a_by_cubes(int(x))
progress = (x - a**3) / ((a+1)**3 - a**3)
progress = max(0, min(1, progress))

col1, col2 = st.columns([3, 1])
with col1:
    st.progress(progress, text=f"{a}³ = {a**3} < {x} < {(a+1)**3} = {a+1}³")
with col2:
    st.metric("정수 부분", a)

with st.expander("🔍 상세 로그"):
    st.dataframe(df_a, use_container_width=True, hide_index=True)

st.divider()

# 4가지 방법
st.markdown("## 🔬 4가지 수사 방법")

tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 방법1: 대입법",
    "📈 방법2: 그래프법", 
    "📐 방법3: 대수근사법",
    "🔁 방법4: 뉴턴법"
])

# Tab 1
with tab1:
    st.markdown("### 직접 대입해서 정답 찾기")
    col1, col2 = st.columns(2)
    
    with col1:
        user_guess = st.slider("b 선택", 0, 9, 3, key="user_guess")
        t_guess = a + user_guess / 10
        result_guess = t_guess ** 3
        next_result = (a + (user_guess+1)/10) ** 3
        
        st.metric(f"t = {t_guess:.1f}", f"t³ = {result_guess:.4f}")
        
        if result_guess < x < next_result:
            st.success(f"🎯 정답!")
        elif result_guess < x:
            st.info(f"✓ {result_guess:.4f} < {x}")
        else:
            st.error(f"✗ {result_guess:.4f} > {x}")
    
    with col2:
        b_sub, df_b, L, U = find_b_by_substitution(int(x), a, b_max=9)
        st.dataframe(df_b, use_container_width=True, hide_index=True)
        st.success(f"🎯 자동 정답: b = {b_sub}")

# Tab 2
with tab2:
    st.markdown("### 곡선에서 교점 찾기")
    
    t_min = max(0.1, a - 0.5)
    t_max = a + 1.5
    ts = np.linspace(t_min, t_max, 500)
    ys = ts**3
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(ts, ys, 'b-', linewidth=3, label='y = t³')
    ax.axhline(y=x, color='r', linestyle='--', linewidth=2, label=f'y = {x}')
    
    for k in range(0, 15):
        ax.axvline(x=a + k/10, color='gray', linestyle=':', alpha=0.3)
    
    ax.plot(true_root, x, 'g*', markersize=20, label='정답', zorder=5)
    
    ax.set_xlabel('t', fontsize=12, fontweight='bold')
    ax.set_ylabel('y', fontsize=12, fontweight='bold')
    ax.set_title('y = t³ 그래프', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.2)
    ax.set_xlim(t_min, t_max)
    
    st.pyplot(fig)

# Tab 3
with tab3:
    st.markdown("### 다항식 전개")
    
    delta = x - a**3
    h = delta / (3*(a**2))
    ten_h = 10*h
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.latex(r"x = a^3 + 3a^2h + ...")
    with col2:
        st.metric("Δ", delta)
        st.metric("h", f"{h:.6f}")
    with col3:
        st.metric("10h", f"{ten_h:.3f}")
        st.metric("b 제안", int(round(ten_h)))

# Tab 4
with tab4:
    st.markdown("### 뉴턴 방법")
    
    t0 = float(t0_custom) if t0_custom else float(a)
    t_final, df_newton = newton_iter(int(x), t0, max_iter, tol)
    
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(df_newton, use_container_width=True, hide_index=True)
    
    with col2:
        iterations = df_newton['반복'].tolist()
        errors = [abs(float(e)) for e in df_newton['오차'].tolist()]
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.semilogy(iterations, errors, 'bo-', linewidth=2, markersize=8)
        ax.set_xlabel('반복', fontsize=12)
        ax.set_ylabel('|오차|', fontsize=12)
        ax.set_title('수렴 속도', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    
    st.success(f"🎉 최종값: t = {t_final:.10f}")

st.divider()
st.markdown("🕵️ SM 수학사무소 | Streamlit 게임 v1.0")
