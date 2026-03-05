import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SM 수학사무소 · 심화 포털", layout="wide")

# ============================
# 설정: 여기만 수정하면 됨
# ============================
ROOT_URL = "https://hamama11.github.io/boostcamp/root근사.html"
LIMIT_URL = "https://hamama11.github.io/boostcamp/limit.html"
REPO_URL = "https://github.com/hamama11/math3"  # 선택: 레포 링크

# ============================
# 헤더
# ============================
st.markdown(
    """
    <div style="padding:24px 28px; border-radius:28px; background:#0b1220; color:#e5e7eb;">
      <div style="display:flex; align-items:center; justify-content:space-between; gap:18px; flex-wrap:wrap;">
        <div style="display:flex; align-items:center; gap:14px;">
          <div style="width:46px; height:46px; border-radius:16px; background:#111827; border:1px solid rgba(255,255,255,0.15);
                      display:flex; align-items:center; justify-content:center; font-weight:900; letter-spacing:0.5px;">
            SM
          </div>
          <div>
            <div style="font-size:34px; font-weight:900; line-height:1.05;">SM 수학사무소 · 심화 탐구 포털</div>
            <div style="margin-top:6px; font-size:15px; color:#a5b4fc; font-weight:800;">
              근사(Approximation) · 오차(Error) · 접선(Tangent)으로 ‘공식의 정당화’까지 추적한다.
            </div>
          </div>
        </div>
        <div style="display:flex; gap:10px; align-items:center;">
          <a href="{repo}" target="_blank"
             style="text-decoration:none; padding:10px 14px; border-radius:14px; background:rgba(255,255,255,0.08);
                    border:1px solid rgba(255,255,255,0.12); color:#e5e7eb; font-weight:900;">
             GitHub
          </a>
        </div>
      </div>
    </div>
    """.replace("{repo}", REPO_URL),
    unsafe_allow_html=True
)

st.write("")

# ============================
# 상단: 미션 보드(심화)
# ============================
col1, col2, col3 = st.columns([1.15, 1.15, 1.0], vertical_alignment="top")

with col1:
    st.subheader("🎯 Mission 1 · 근사의 설계")
    st.markdown(
        """
        **목표**: \(\sqrt[3]{x}\)를 빠르게 근사하고, 그 근사가 왜 먹히는지 설명한다.  
        **핵심 질문**  
        - 어떤 \(n\)을 잡아야 오차가 줄어드는가?  
        - \((n+h)^3\) 전개에서 무엇을 버려도 되는가?  
        - “정확도 10%” 같은 기준을 수학적으로 어떻게 정하나?
        """
    )
    st.link_button("🧩 Root 근사(활동) 바로가기", ROOT_URL, use_container_width=True)
    st.caption("iframe이 안 보이면 위 버튼으로 직접 열기")

with col2:
    st.subheader("🧪 Mission 2 · 검증과 보정")
    st.markdown(
        """
        **검증**: 근사값 \(y\)에 대해 실제 오차 \(\;y^3-x\;\)의 부호/크기를 해석한다.  
        **보정**: 선형 근사 1회로 부족하면 **반복(Iteration)** 을 설계한다.  
        - 1차: \(y_1 = n + \frac{x-n^3}{3n^2}\)  
        - 2차(선택): \(y_2 = y_1 + \frac{x-y_1^3}{3y_1^2}\)  (뉴턴 업데이트 형태)
        """
    )
    st.link_button("📉 Limit(접선/변화율) 연결 활동", LIMIT_URL, use_container_width=True)
    st.caption("근사 = 접선(선형화) 관점으로 정당화")

with col3:
    st.subheader("🧭 운영 가이드(교사용)")
    st.info(
        """
        **수업 흐름(심화형)**  
        1) 정수 경계(하한/상한) 먼저 포착  
        2) 오차 부호로 ‘과대/과소’ 판단  
        3) 전개식에서 버리는 항의 조건 명시  
        4) 접선(미분)으로 공식 정당화  
        5) 반복 보정(선택)으로 확장  
        """,
        icon="🧩"
    )
    st.markdown("**빠른 링크**")
    st.link_button("Root 페이지 열기", ROOT_URL, use_container_width=True)
    st.link_button("Limit 페이지 열기", LIMIT_URL, use_container_width=True)

st.divider()

# ============================
# 심화 과제 카드
# ============================
st.subheader("🧠 심화 과제(탐구/보고서용)")
a, b, c = st.columns(3)

with a:
    st.markdown("### A. 오차의 ‘버려도 됨’ 조건 만들기")
    st.markdown(
        """
        \((n+h)^3 = n^3 + 3n^2h + 3nh^2 + h^3\) 에서  
        **왜** \(h^2, h^3\)를 버리는지, **언제** 버리면 안 되는지 조건을 세워라.  
        - 예: \(|h| \le 0.1\)일 때 \(|3nh^2 + h^3|\) 상계 추정
        """
    )

with b:
    st.markdown("### B. ‘최적 n 선택’ 규칙 만들기")
    st.markdown(
        """
        \(x\)가 주어졌을 때 \(n\)을 **floor/round/ceil** 중 어떻게 잡는 게 좋은가?  
        - 상대오차 기준 vs 절대오차 기준  
        - \(x\in[8,27]\)에서 \(n=2\) 고정이 왜 합리적인가?
        """
    )

with c:
    st.markdown("### C. 반복 보정(뉴턴) 2회로 정확도 비교")
    st.markdown(
        """
        \(y_{k+1}=y_k+\frac{x-y_k^3}{3y_k^2}\) 를 1회/2회 적용해  
        정확도가 얼마나 개선되는지 표·그래프로 비교하라.  
        - 추천 실험: \(x=12, 15, 20\)
        """
    )

st.divider()

# ============================
# 미리보기(탭)
# ============================
st.subheader("🔎 미리보기(수업 현장용)")
tab1, tab2 = st.tabs(["Root 근사", "Limit/접선 연결"])

with tab1:
    st.caption("안 보이면 상단 버튼으로 직접 열기")
    components.iframe(src=ROOT_URL, height=1750, scrolling=True)

with tab2:
    st.caption("안 보이면 상단 버튼으로 직접 열기")
    components.iframe(src=LIMIT_URL, height=1750, scrolling=True)

st.divider()

# ============================
# 하단: 체크리스트 + 평가요소
# ============================
st.subheader("✅ 평가 요소(심화)")
st.markdown(
    """
    - **개념 이해**: 근사가 ‘선형화(접선)’라는 관점으로 설명됨  
    - **오차 분석**: 오차의 부호/크기를 해석하고 근거를 제시함  
    - **조건 설정**: \(h^2,h^3\)을 버리는 ‘경계 조건’을 수학적으로 제시함  
    - **확장 탐구**: 반복 보정(뉴턴) 또는 다른 근사법 비교로 확장함  
    - **소통**: 계산·그래프·문장을 연결해 논리적으로 보고함  
    """
)

st.caption("© SM Math Office · 심화 탐구 포털")
