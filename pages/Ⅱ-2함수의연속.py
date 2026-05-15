import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🌊 함수의 연속 : 미시와 거시의 시선")

st.markdown("""
<p style='font-size:18px; font-weight:500; line-height:2; margin-bottom:10px;'>
함수의 극한은 한 점을 향해 아주 가까이 다가가는 <b>미시적 관찰</b>에서 시작됩니다.<br>
그러나 그 작은 움직임을 따라가다 보면, 그래프 전체의 흐름과 구조를 바라보는 <b>거시적 이해</b>로 이어집니다.
</p>
""", unsafe_allow_html=True)

# 슬라이드 1~8
for i in range(1, 9):
    st.image(
        f"assets/함수의연속/images/슬라이드{i}.PNG",
        use_container_width=True
    )
