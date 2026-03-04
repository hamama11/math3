import math
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="SM 수학사무소: 세제곱근 수사 전략", layout="wide")

# ---------- Helpers ----------
def cbrt(x: float) -> float:
    return x ** (1/3)

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def linear_approx_cuberoot(x: float, n: float) -> float:
    # x ≈ n^3 + 3n^2 h  =>  h ≈ (x - n^3)/(3n^2)
    if n == 0:
        return 0.0
    return n + (x - n**3) / (3 * n**2)

def radar_bounds(x: float):
    r = cbrt(x)
    n = int(math.floor(r))
    if n < 0:
        n = 0
    lower = n**3
    upper = (n+1)**3
    # 위치(%) : lower~upper에서 x가 어디쯤
    percent = 0.0 if upper == lower else (x - lower) / (upper - lower)
    return n, lower, upper, clamp(percent, 0.0, 1.0)

# ---------- UI: Header ----------
st.markdown(
    """
    <div style="padding:18px 22px; border-radius:24px; background:#ffffff; border:1px solid #e5e7eb;">
      <div style="font-size:34px; font-weight:900; margin-bottom:6px;">SM 수학사무소</div>
      <div style="font-size:18px; color:#6b7280; font-weight:700;">
        정밀 수치 수사: <span style="color:#4f46e5;">∛x</span>의 비밀번호를 포착하세요.
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
colA, colB, colC = st.columns([1.1, 1.1, 1.0], vertical_alignment="top")

# ---------- Global Target ----------
with colA:
    st.subheader("수사 대상 설정")
    x = st.number_input("추적할 숫자 x", min_value=1.0, max_value=500.0, value=12.0, step=1.0)
    exact_root = cbrt(x)

    # 초기 추측값(세션 유지)
    if "y_guess" not in st.session_state:
        st.session_state.y_guess = float(exact_root)

    # 추측값 범위: 정답 근처 ±1.5
    start = max(0.0, exact_root - 1.5)
    end = exact_root + 1.5

    # 추측값 조절(드래그 대신 슬라이더)
    st.session_state.y_guess = st.slider(
        "추측값 y (좌우 조절)",
        min_value=float(start),
        max_value=float(end),
        value=float(clamp(st.session_state.y_guess, start, end)),
        step=0.001,
    )

    y = float(st.session_state.y_guess)
    y3 = y**3
    err = y3 - x

    st.markdown(
        f"""
        <div style="padding:14px 16px; border-radius:18px; background:#0f172a; color:#fff;">
          <div style="font-size:13px; opacity:0.7; font-weight:700;">Current Status</div>
          <div style="margin-top:8px; font-family:monospace; font-size:18px;">P({y:.3f}, {y3:.3f})</div>
          <div style="margin-top:10px; display:inline-block; padding:6px 10px; border-radius:12px;
               background: {'rgba(16,185,129,0.20)' if abs(err)<0.1 else 'rgba(239,68,68,0.20)'};
               color: {'#34d399' if abs(err)<0.1 else '#fca5a5'}; font-weight:900;">
            오차: {('+' if err>0 else '')}{err:.3f}
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- Radar ----------
with colB:
    st.subheader("정수 거듭제곱 구간 탐지 레이더")
    n, lower, upper, p = radar_bounds(x)

    st.caption(f"추측 범위: **{n}.x**  ( {lower} = {n}³ , {upper} = {n+1}³ )")

    # 레이더 바(HTML)
    st.markdown(
        f"""
        <div style="padding:16px; border-radius:20px; background:#111827; border:1px solid #1f2937;">
          <div style="position:relative; height:14px; background:#0b1220; border-radius:999px;">
            <div style="position:absolute; left:0; top:0; height:14px; width:{p*100:.1f}%;
                        background:rgba(99,102,241,0.55); border-radius:999px;"></div>
            <div style="position:absolute; left:{p*100:.1f}%; top:50%; transform:translate(-50%,-50%);
                        width:18px; height:18px; border-radius:999px; background:#fbbf24;
                        box-shadow:0 0 18px rgba(251,191,36,0.85);"></div>
          </div>
          <div style="display:flex; justify-content:space-between; margin-top:10px; color:#c7d2fe; font-weight:900;">
            <div>{lower} <span style="opacity:0.7; font-weight:800;">({n}³)</span></div>
            <div>x = {x:g}</div>
            <div>{upper} <span style="opacity:0.7; font-weight:800;">({n+1}³)</span></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.subheader("Method 1: 대입 수사 (수치 대조)")

    # 막대 그래프
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(y=["추측 (y³)", "목표 (x)"], x=[y3, x], orientation="h"))
    fig1.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig1, use_container_width=True)

# ---------- Methods 2~4 ----------
with colC:
    st.subheader("Method 2: 기하학 수사 (그래프 추적)")
    # 곡선 y = t^3, t in [start, end]
    xs = [start + (end-start)*i/120 for i in range(121)]
    ys = [t**3 for t in xs]
    minY, maxY = min(ys), max(ys)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name="y = t³"))
    # 목표점
    fig2.add_trace(go.Scatter(x=[exact_root], y=[x], mode="markers", name="목표 지점", marker=dict(size=10)))
    # 탐지선(수직선)
    fig2.add_trace(go.Scatter(x=[y, y], y=[minY, maxY], mode="lines", name="탐지선", line=dict(dash="dash")))
    fig2.update_layout(height=320, margin=dict(l=10, r=10, t=10, b=10),
                       xaxis_title="추측값 y", yaxis_title="세제곱 y³")
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.subheader("Method 3: 대수적 수사 (선형 근사)")
    # n 선택: 정답 근처 정수로 기본
    n0 = max(1.0, float(round(exact_root)))
    n_in = st.number_input("가까운 정수 n", min_value=1.0, max_value=50.0, value=float(n0), step=1.0)

    approx = linear_approx_cuberoot(x, n_in)
    actual = exact_root
    acc = 100.0
    if actual > 1e-9:
        acc = (1 - abs(actual - approx)/actual) * 100
    acc = clamp(acc, 0.0, 100.0)

    st.latex(rf"\sqrt[3]{{{x:g}}} \approx {n_in:g} + \frac{{{(x - n_in**3):g}}}{{3\cdot ({n_in:g})^2}} = {approx:.6f}")
    st.progress(acc/100.0, text=f"분석 정확도(상대): {acc:.3f}%")

    st.divider()

    st.subheader("Method 4: 미분 수사 (접선 연결)")
    st.latex(r"f(x)=x^{1/3},\quad f'(x)=\frac{1}{3}x^{-2/3}")
    st.markdown(
        """
        - 위 대수 근사는 사실상 **접선 근사**(선형화)입니다.  
        - 점 \(a=n^3\)에서 접선 \(y=f(a)+f'(a)(x-a)\)를 쓰면  
          \(\;y \approx n + \dfrac{x-n^3}{3n^2}\) 가 그대로 나옵니다.
        """
    )
