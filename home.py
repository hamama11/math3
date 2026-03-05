import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SM 수학사무소 · 활동 포털", layout="wide")

# ----------------------------
# 설정: 여기만 바꾸면 됨
# ----------------------------
ROOT_URL = "https://hamama11.github.io/boostcamp/root근사.html"
LIMIT_URL = "https://hamama11.github.io/boostcamp/limit.html"

# ----------------------------
# 헤더(대문)
# ----------------------------
st.markdown(
    """
    <div style="padding:22px 26px; border-radius:26px; background:#ffffff; border:1px solid #e5e7eb;">
      <div style="display:flex; align-items:center; gap:14px;">
        <div style="width:44px; height:44px; border-radius:14px; background:#111827; display:flex; align-items:center; justify-content:center; color:white; font-weight:900;">
          SM
        </div>
        <div>
          <div style="font-size:34px; font-weight:900; line-height:1.05;">SM 수학사무소</div>
          <div style="margin-top:6px; font-size:16px; color:#6b7280; font-weight:700;">
            활동 포털 · 링크가 막히면 아래 ‘직접 열기’로 바로 이동하세요.
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ----------------------------
# 상단: 오늘의 활동 / 바로 시작
# ----------------------------
left, right = st.columns([1.2, 1.0], vertical_alignment="top")

with left:
    st.subheader("🚀 오늘의 활동")
    st.markdown(
        """
        - **Root 근사 추적**: 정수 경계에서 근사값을 ‘수사’하듯 추적하기  
        - **Limit(극한) 시각화**: 변화율·접선·근사 아이디어 연결  
        - 왼쪽 사이드바에서 단원별 페이지로 이동 가능
        """
    )

    st.markdown("#### ✅ 바로 시작")
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🧩 Root 근사 열기", ROOT_URL, use_container_width=True)
        st.caption("GitHub Pages로 직접 열기")
    with c2:
        st.link_button("📉 Limit 활동 열기", LIMIT_URL, use_container_width=True)
        st.caption("GitHub Pages로 직접 열기")

with right:
    st.subheader("🧭 사용 안내")
    st.info(
        """
        1) 아래 미리보기(iframe)가 안 보이면 위 ‘직접 열기’ 버튼을 누르세요.  
        2) 모바일은 스크롤이 길 수 있어요.  
        3) 수업 중에는 **오차(+) / 오차(-)** 의미를 반드시 체크!
        """,
        icon="ℹ️"
    )

st.divider()

# ----------------------------
# 활동 카드(포털 느낌)
# ----------------------------
st.subheader("🗂️ 활동 모음")

card1, card2, card3 = st.columns(3)

with card1:
    st.markdown("### 🧩 Root 근사")
    st.caption("정수의 세제곱 사이에서 세제곱근/제곱근을 추적")
    st.markdown("- 대입 ➝ 그래프 ➝ 대수 전개 ➝ 미분(접선) 연결")
    st.link_button("열기", ROOT_URL, use_container_width=True)

with card2:
    st.markdown("### 🧾 지수·로그 (pages)")
    st.caption("왼쪽 사이드바 페이지로 이동")
    st.markdown("- `pages/1.지수log.py` 에서 활동 진행")
    st.warning("사이드바에서 선택하세요.", icon="➡️")

st.divider()

# ----------------------------
# 미리보기(iframe) - 탭으로 구성
# ----------------------------
st.subheader("🔎 미리보기")

tab1, tab2 = st.tabs(["Root 근사", "Limit"])

with tab1:
    st.caption("화면이 안 보이면 위 ‘직접 열기’ 버튼으로 이동하세요.")
    components.iframe(src=ROOT_URL, height=1800, scrolling=True)

with tab2:
    st.caption("화면이 안 보이면 위 ‘직접 열기’ 버튼으로 이동하세요.")
    components.iframe(src=LIMIT_URL, height=1800, scrolling=True)

st.divider()

# ----------------------------
# 하단: 수업용 체크리스트
# ----------------------------
st.subheader("✅ 수업 체크리스트(교사용)")
st.markdown(
    """
    - [ ] 학생이 먼저 **정수 경계(하한/상한)** 를 찾게 했다  
    - [ ] 오차의 부호(+, -)가 의미하는 바를 말하게 했다  
    - [ ] 대수 근사에서 왜 \(h^2, h^3\) 를 버리는지 ‘조건’을 언급했다  
    - [ ] 미분(접선)으로 공식이 연결된다는 것을 한 문장으로 정리시켰다  
    """
)

st.caption("© SM Math Office · 수업용 포털")
