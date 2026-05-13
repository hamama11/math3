import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🌊 함수의 극한 : 미시와 거시의 시선")

st.markdown("""
<p style='font-size:18px; font-weight:500; line-height:2; margin-bottom:10px;'>
함수의 극한은 한 점을 향해 아주 가까이 다가가는 <b>미시적 관찰</b>에서 시작됩니다.<br>
그러나 그 작은 움직임을 따라가다 보면, 그래프 전체의 흐름과 구조를 바라보는 <b>거시적 이해</b>로 이어집니다.
</p>
""", unsafe_allow_html=True)

# 슬라이드 1~2
for i in range(1, 3):
    st.image(
        f"assets/함수의극한/images/슬라이드{i}.PNG",
        use_container_width=True
    )

# HTML 읽기
with open(
    "assets/함수의극한/html/p14_lv2_q4.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

wrapped_html = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html}
</div>
"""

st.markdown("---")

# 슬라이드3 + HTML 좌우 배치
left, right = st.columns([1, 1.2])

with left:
    st.image(
        "assets/함수의극한/images/슬라이드3.PNG",
        use_container_width=True
    )

with right:
    with st.expander("🔍 직접 탐구해보기", expanded=False):

        components.html(
            wrapped_html,
            height=650,
            scrolling=True
        )

st.markdown("---")

# 슬라이드 4~5
for i in range(4, 6):
    st.image(
        f"assets/함수의극한/images/슬라이드{i}.PNG",
        use_container_width=True
    )


# HTML 읽기
with open(
    "assets/함수의극한/html/power.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

wrapped_html = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html}
</div>
"""

st.markdown("---")

# 슬라이드6 + HTML 좌우 배치
left, right = st.columns([1, 1])

with left:
    st.image(
        "assets/함수의극한/images/슬라이드6.PNG",
        use_container_width=True
    )

with right:
    with st.expander("🔍 직접 탐구해보기", expanded=False):

        components.html(
            wrapped_html,
            height=650,
            scrolling=True
        )

st.markdown("---")
# 슬라이드 7
for i in range(7, 8):
    st.image(
        f"assets/함수의극한/images/슬라이드{i}.PNG",
        use_container_width=True
    )
