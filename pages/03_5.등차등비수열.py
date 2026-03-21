import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide")

# 경로 설정 (pages 기준)
BASE_DIR = Path(__file__).resolve().parent.parent

# 제목
st.title("🌠 탐구자들이여, 수의 흐름을 살피라")
st.markdown(
    """
    <p style='font-size:18px; font-weight:500; line-height:2;'>
    수는 이어지고, 그 이어짐 속에 법도가 깃들어 있도다.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# HTML 1
with open(BASE_DIR / "s_n,a_n.html", encoding="utf-8") as f:
    html1 = f.read()

components.html(html1, height=700, scrolling=True)

# HTML 2
with open(BASE_DIR / "a_2n.html", encoding="utf-8") as f:
    html2 = f.read()

components.html(html2, height=700, scrolling=True)
