import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
# 🌌 헤더
st.title("📈 미분계수와 도함수 : 변화율의 극한")

# 🌿 머리말
st.markdown("""
<p style='font-size:19px; line-height:2;'>

🌌 <b>변화란 과연 무엇인고?</b><br><br>

세상은 끊임없이 변하고 흐르건만,<br>
우리는 그 움직임을 어떻게 붙잡을 수 있겠느냐.<br><br>

두 순간 사이의 변화는 볼 수 있으나,<br>
우리가 진정 알고자 했던 것은 ‘바로 이 순간’의 변화였도다.<br><br>

점점 더 가까워지고,<br>
또 가까워질수록,<br>
변화율은 하나의 값으로 향하기 시작하니,<br>
이를 우리는 변화율의 극한이라 부르도다.<br><br>

미분계수란 결국,<br>
순간 속에 숨어 있는 변화의 방향과 속도를 읽어내려는 시도이며,<br>
도함수란 그러한 순간들이 이어져 만들어낸 흐름의 기록이 아니겠느냐.

</p>
""", unsafe_allow_html=True)

st.markdown("---")

# 🖼 슬라이드 1
    st.image(
        f"assets/미분계수와도함수/images/슬라이드1.PNG",
        use_container_width=True
    )
# 좌우 배치
left, right = st.columns([1, 1.2])

with left:
    st.image(
        "assets/미분계수와도함수/images/슬라이드2.PNG",
        use_container_width=True
    )

with right:
    with st.expander("🔍 풀이", expanded=False):

         st.image(
        "assets/미분계수와도함수/images/슬라이드2-3.PNG",
        use_container_width=True
    )

# HTML 불러오기
html_path = "assets/미분계수와도함수/html/미분계수.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

wrapped_html = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html_content}
</div>
"""

with st.expander("🔍미분계수 뿌시기", expanded=False):
    components.html(
        wrapped_html,
        height=900,
        scrolling=True
    )

st.markdown("---")

st.markdown("""
<p style='font-size:18px; line-height:1.9;'>

🔍 <b>가까워질수록 더 선명해지는 것이 있도다.</b><br><br>

찰나에 가까워질수록,<br>
우리는 비로소 변화의 진짜 방향을 마주하게 되도다.

</p>
""", unsafe_allow_html=True)

st.markdown("---")

# 🖼 슬라이드 3~5
for i in range(3, 6):
    st.image(
        f"assets/미분계수와도함수/images/슬라이드{i}.PNG",
        use_container_width=True
    )


# HTML 불러오기
html_path = "assets/미분계수와도함수/html/2종불연속.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

wrapped_html = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html_content}
</div>
"""

with st.expander("🔍lim f' vs f'", expanded=False):
    components.html(
        wrapped_html,
        height=900,
        scrolling=True
    )
