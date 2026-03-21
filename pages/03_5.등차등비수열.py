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
    흐름을 살피노라면 마침내 숨은 이치가 드러나느니라.
    수는 이어지고, 연이 있다면 그 이어짐 속에 인연도 깃들어 있지 않겠는가.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# ✅외부 URL1
components.iframe(
    "https://gemini.google.com/share/ff32a6765473",
    height=900,  
    scrolling=True
)


# 🔥 HTML 1
with open(BASE_DIR / "5.s_n,a_n.html", encoding="utf-8") as f:
    html1 = f.read()

st.markdown("---")
st.subheader("① 수열의 흐름을 좇아")
components.html(html1, height=700, scrolling=True)


# 구분
st.markdown("---")
st.markdown(
    "<h3 style='text-align:center;'>이제 그 이치를 갈라 살필 차례로다</h3>",
    unsafe_allow_html=True
)
st.markdown("---")


# 🔥 HTML 2
with open(BASE_DIR / "5.a_2n.html", encoding="utf-8") as f:
    html2 = f.read()

st.subheader("② 짝과 홀의 갈림 속에 숨은 것들")
components.html(html2, height=700, scrolling=True)
