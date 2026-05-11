import streamlit as st
import streamlit.components.v1 as components

st.title("🧩 Root 제곱근/세제곱근 근사 추적")
st.markdown(
    """
    **배움의 도(道)는 잠시 가려질지언정 끊어지지 아니하나니, 뜻을 세운 이라면 기필코 확인하여 탐구를 이어가시기 바라옵니다.**
    """,
    unsafe_allow_html=True
)
with open("newton.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=2200, scrolling=True)
