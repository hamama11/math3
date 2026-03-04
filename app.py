import math
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="세제곱근 소수 첫째자리 실습", layout="wide")

st.title("세제곱근 소수 첫째자리 찾기 실습")
st.caption("대입 · 그래프 · 대수 근사 · 뉴턴 근사 (가우스 기호/이진탐색 없이)")

def cube_root(x: float) -> float:
    return x ** (1/3)

def find_a_by_cubes(x: int):
    """Find natural number a such that a^3 < x < (a+1)^3."""
    a = 1
    rows = []
    while True:
        left = a**3
        right = (a+1)**3
        rows.append({"a": a, "a^3": left, "(a+1)^3": right, "condition": f"{left} < {x} < {right}"})
        if left < x < right:
            return a, pd.DataFrame(rows)
        a += 1
        if a > 100000:
            raise ValueError("a search exceeded limit")

def find_b_by_substitution(x: int, a: int, b_max: int = 8):
    """Sequentially find b in [0,b_max] such that (a+b/10)^3 < x < (a+(b+1)/10)^3."""
    rows = []
    chosen_b = None
    for b in range(0, b_max+1):
        t = a + b/10
        val = t**3
        ok = val < x
        rows.append({"b": b, "t = a + b/10": t, "t^3": val, "t^3 < x ?": ok})
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
    """Linear (tangent-like) guess for h and a nearby integer b0 around 10h."""
    delta = x - a**3
    denom = 3*(a**2)
    h = delta / denom
    ten_h = 10*h
    b0 = int(round(ten_h))
    return delta, h, ten_h, b0

def algebraic_quadratic_upper_h(x: int, a: int):
    """
    From delta = 3a^2 h + 3a h^2 + h^3 > 3a^2 h + 3a h^2,
    solve 3a h^2 + 3a^2 h - delta = 0. Positive root gives an upper bound for h.
    """
    delta = x - a**3
    A = 3*a
    B = 3*(a**2)
    C = -delta
    disc = B*B - 4*A*C
    h_plus = (-B + math.sqrt(disc)) / (2*A) if A != 0 else delta / B
    return delta, disc, h_plus

def newton_iter(x: int, t0: float, max_iter: int = 6, tol: float = 1e-10):
    """Newton iterations for f(t)=t^3-x. Returns final t and a log dataframe."""
    rows = []
    t = t0
    for k in range(max_iter):
        t3 = t**3
        err = t3 - x
        rows.append({"iter": k, "t": t, "t^3": t3, "t^3 - x": err})
        if abs(err) < tol:
            break
        t = t + (x - t3) / (3*(t**2))
    t3 = t**3
    err = t3 - x
    rows.append({"iter": k+1, "t": t, "t^3": t3, "t^3 - x": err})
    return t, pd.DataFrame(rows)

def suggest_b_from_t(t: float, a: int, b_max: int):
    """
    Suggest b satisfying a + b/10 <= t < a + (b+1)/10 (internal integer ops).
    UI will present it as an inequality, not with floor symbols.
    """
    ten_h = 10*(t - a)
    b = int(math.floor(ten_h))
    b = max(0, min(b, b_max))
    return b, ten_h

# -----------------------------
# Sidebar inputs
# -----------------------------
with st.sidebar:
    st.header("입력")
    x = st.number_input("추론할 자연수 x", min_value=2, value=15, step=1)
    assume_b_le_8 = st.checkbox("문제 조건: b ≤ 8 적용", value=True)
    b_max = 8 if assume_b_le_8 else 9

    st.divider()
    st.subheader("뉴턴 근사 설정")
    max_iter = st.slider("반복 횟수", min_value=1, max_value=12, value=6)
    tol_pow = st.select_slider("중지 기준 |t^3 - x|", options=[-2, -4, -6, -8, -10, -12], value=-10)
    tol = 10.0**tol_pow
    use_custom_t0 = st.checkbox("초기값 t0 직접 입력", value=False)
    t0_custom = st.number_input("t0", value=3.0, step=0.1, disabled=not use_custom_t0)

st.markdown("### 공통 정의")
st.latex(r"a^3 < x < (a+1)^3,\quad \left(a+\frac{b}{10}\right)^3 < x < \left(a+\frac{b+1}{10}\right)^3")

approx_true = cube_root(float(x))
if abs(round(approx_true)**3 - x) < 1e-12:
    st.warning("입력한 x는 완전세제곱수입니다. (엄격부등식에서는 경계에 걸릴 수 있어요.) 그래도 실습은 진행합니다.")

# -----------------------------
# Step 1: find a
# -----------------------------
a, df_a = find_a_by_cubes(int(x))

col1, col2, col3 = st.columns([1.2, 1.2, 1.6])
with col1:
    st.subheader("결과 요약")
    st.write(f"- 입력 x = **{int(x)}**")
    st.write(f"- 정수 부분 a는 **{a}** (즉, {a}^3 < x < {a+1}^3)")
    st.write(f"- (검산용) √[3]x ≈ **{approx_true:.6f}**")
with col2:
    st.subheader("a 찾기 로그(세제곱 비교)")
    st.dataframe(df_a, use_container_width=True, height=240)
with col3:
    st.subheader("최종 목표")
    st.write(f"다음 자연수 b(0~{b_max})를 찾아서")
    st.latex(r"\left(a+\frac{b}{10}\right)^3 < x < \left(a+\frac{b+1}{10}\right)^3")
    st.write("를 만족시키면, 세제곱근의 소수 첫째 자리가 결정됩니다.")

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["1) 대입", "2) 그래프", "3) 대수 근사", "4) 뉴턴 근사", "부록(하한/반례)"]
)

# -----------------------------
# 1) Substitution
# -----------------------------
with tab1:
    st.subheader("1) 대입(순차 비교)")
    b_sub, df_b, L, U = find_b_by_substitution(int(x), a, b_max=b_max)
    ok = (L < x < U)
    st.write(f"**결론:** b = **{b_sub}**")
    st.write(f"검증: (a + b/10)^3 = {L:.6f}  <  x = {int(x)}  <  (a + (b+1)/10)^3 = {U:.6f}  ➜  {ok}")
    st.dataframe(df_b, use_container_width=True, height=280)

# -----------------------------
# 2) Graph
# -----------------------------
with tab2:
    st.subheader("2) 그래프(시각화)")
    st.write("그래프 y=t^3 와 y=x 의 교점을 보고, 0.1 간격 격자에서 어느 구간인지 확인합니다.")
    t_min = a
    t_max = a + 1
    ts = np.linspace(t_min, t_max, 400)
    ys = ts**3

    fig, ax = plt.subplots()
    ax.plot(ts, ys, label="y = t^3")
    ax.axhline(y=float(x), label="y = x")
    for k in range(0, 10):
        ax.axvline(x=a + k/10, linestyle="--", linewidth=0.8)
    ax.scatter([approx_true], [float(x)], s=40)
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.set_title("t in [a, a+1] with 0.1 grid")
    ax.set_xlim(t_min, t_max)
    ax.set_ylim(min(ys.min(), float(x))*0.98, max(ys.max(), float(x))*1.02)
    ax.legend()
    st.pyplot(fig, clear_figure=True)

    st.write("대입 결과로 확인된 구간:")
    st.latex(rf"{a}+{b_sub}/10 < \sqrt[3]{{{int(x)}}} < {a}+{b_sub+1}/10")

# -----------------------------
# 3) Algebraic approximation
# -----------------------------
with tab3:
    st.subheader("3) 대수 근사(전개 기반 출발점)")
    delta, h_lin, ten_h, b0 = algebraic_linear_guess_b(int(x), a)
    st.write("전개식")
    st.latex(r"x-a^3 = 3a^2h + 3ah^2 + h^3")
    st.write("1차 근사(접선 느낌): 작은 항을 잠깐 무시하고 출발점만 잡습니다.")
    st.latex(r"h \approx \frac{x-a^3}{3a^2}")

    st.write(f"- Δ = x - a^3 = **{delta}**")
    st.write(f"- 근사 h ≈ **{h_lin:.6f}**  (따라서 10h ≈ **{ten_h:.3f}**)")
    st.write(
        f"- 출발점 제안: 10h가 {b0} 근처이므로, b를 {max(0, min(b0, b_max))} 근처에서 대입으로 확인합니다."
    )
    st.caption("주의: 이 근사는 '정답 확정'이 아니라 '대입 시작점' 추천용입니다.")

    st.divider()
    st.write("2차까지 반영한 상한(참고):")
    delta2, disc, h_plus = algebraic_quadratic_upper_h(int(x), a)
    st.write("h^3>0 이므로  h^3를 버리면  Δ > 3a^2h + 3ah^2  를 얻습니다.")
    st.latex(r"3ah^2 + 3a^2h - (x-a^3) < 0")
    st.write(f"- 판별식 D = **{disc:.3f}**")
    st.write(f"- 양의 근 h₊ = **{h_plus:.6f}**  (즉, h < h₊)")
    st.write(f"- 따라서 10h < **{10*h_plus:.3f}**  이라 b의 가능한 상한을 더 줄일 수 있습니다.")
    st.caption("여기서도 마지막 확정은 '대입(0.1 간격 세제곱 비교)'으로 합니다.")

# -----------------------------
# 4) Newton approximation
# -----------------------------
with tab4:
    st.subheader("4) 뉴턴 근사(접선 반복)")
    st.write("f(t)=t^3-x 의 근을 접선으로 반복해서 찾는 방법입니다.")
    st.latex(r"t_{new} = t + \frac{x-t^3}{3t^2}")

    t0 = float(t0_custom) if use_custom_t0 else float(a)
    t_final, df_newton = newton_iter(int(x), t0, max_iter=max_iter, tol=tol)
    st.write(f"- 초기값 t0 = **{t0:.6f}**")
    st.write(f"- 최종값 t ≈ **{t_final:.10f}**  (검산용 실제 √[3]x ≈ {approx_true:.10f})")

    b_suggest, ten_h_new = suggest_b_from_t(t_final, a, b_max)
    st.write("이 값으로부터 0.1 구간 후보를 제안합니다:")
    st.write(f"- t - a ≈ {t_final-a:.6f}  →  10(t-a) ≈ {ten_h_new:.3f}")
    st.write(f"- 따라서 b는 {b_suggest} 근처. (최종은 대입으로 확인)")

    st.divider()
    st.write("대입으로 최종 확정(제안 b부터 근처만 확인):")
    candidates = sorted(set([max(0, b_suggest-1), b_suggest, min(b_max, b_suggest+1)]))
    rows = []
    final_b = None
    for b in candidates:
        Lc = (a + b/10)**3
        Uc = (a + (b+1)/10)**3
        okc = (Lc < x < Uc)
        rows.append({"b": b, "(a+b/10)^3": Lc, "(a+(b+1)/10)^3": Uc, "interval ok?": okc})
        if okc:
            final_b = b
    if final_b is None:
        final_b = b_sub
    st.write(f"**결론:** b = **{final_b}**")
    st.dataframe(pd.DataFrame(rows), use_container_width=True)
    st.divider()
    st.dataframe(df_newton, use_container_width=True, height=280)

# -----------------------------
# Appendix: lower bound and counterexample
# -----------------------------
with tab5:
    st.subheader("부록: 하한(읽기자료) & 반례")

    st.markdown("### 1) 하한(읽기자료)")
    st.write("0 < h < 1 이면  h^2 < h,  h^3 < h  이므로")
    st.latex(r"x-a^3=3a^2h+3ah^2+h^3 < 3a^2h+3ah+h = h(3a^2+3a+1)")
    st.write("따라서")
    st.latex(r"\frac{x-a^3}{3a^2+3a+1} < h")
    st.caption("이 하한은 실습 로직(정답 확정)에는 사용하지 않고, 읽기자료로만 제공합니다.")

    st.divider()
    st.markdown("### 2) 반례: 너무 단순한 하한은 항상 맞지 않다")
    st.write("예를 들어 다음과 같은 주장(단순화)은 항상 성립하지 않습니다.")
    st.latex(r"h > \frac{x-a^3}{3a^2+1}")
    st.write("아래 버튼을 누르면 반례를 보여줍니다. (a=1에서 h가 큰 경우)")
    if st.button("반례 실행"):
        a_ce = 1
        h_ce = 0.9
        x_ce = (a_ce + h_ce)**3
        lhs = h_ce
        rhs = (x_ce - a_ce**3) / (3*(a_ce**2) + 1)
        st.write(f"- 선택: a = {a_ce}, h = {h_ce} → x = (a+h)^3 ≈ {x_ce:.6f}")
        st.write(f"- 좌변 h = {lhs:.6f}")
        st.write(f"- 우변 (x-a^3)/(3a^2+1) ≈ {rhs:.6f}")
        st.write(f"비교: h > (x-a^3)/(3a^2+1)  는  **{lhs > rhs}** (거짓이면 반례 성립)")
