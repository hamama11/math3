import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# 🌊 제목
st.title("🌊 함수의 연속 : 미시와 거시의 시선")

# 🌌 머리말
st.markdown("""
<p style='font-size:19px; line-height:2;'>

🌌 <b>연속이란 무엇인고?</b><br><br>

사람의 마음도,<br>
어제의 나와 오늘의 내가 이어져 있기에 같은 삶이라 부르는 것이 아니더냐.<br><br>

작은 흔들림과 변화가 있어도,<br>
그 흐름이 완전히 끊어지지 않는다면 우리는 계속 앞으로 나아갈 수 있도다.<br><br>

세상 모든 것은 조금씩 변하고 흔들리나,<br>
그 안에서도 이어지는 무언가가 있기에 관계와 삶은 유지되는 것이 아니겠느냐.

</p>
""", unsafe_allow_html=True)

st.markdown("---")

# 🖼 슬라이드 1~4
for i in range(1, 5):
    st.image(
        f"assets/함수의연속/images/슬라이드{i}.PNG",
        use_container_width=True
    )

# 🔍 중간 질문
st.markdown("""
<p style='font-size:18px; line-height:1.9;'>

🔍 <b>정말 끊어졌다고 말할 수 있는가?</b><br><br>

아주 작은 틈이 존재한다 하여,<br>
그 흐름 전체가 사라졌다고 말할 수 있겠는가.

</p>
""", unsafe_allow_html=True)

st.markdown("---")

# HTML 읽기
with open(
    "assets/함수의연속/html/분모0.html",
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

# 좌우 배치
left, right = st.columns([1, 1])

with left:
    st.image(
        "assets/함수의연속/images/슬라이드6.PNG",
        use_container_width=True
    )

with right:
    with st.expander("🔍 복습", expanded=False):

        components.html(
            wrapped_html,
            height=650,
            scrolling=True
        )

st.markdown("---")
    
# 🖼 슬라이드 7~8
for i in range(7, 9):
    st.image(
        f"assets/함수의연속/images/슬라이드{i}.PNG",
        use_container_width=True
    )
