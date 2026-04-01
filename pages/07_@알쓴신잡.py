import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide")

# 추후 외부 URL
url1 = "https://gemini.google.com/share/e8ed4a3c08d7"

# 제목 + 설명
st.markdown("""
<p style='font-size:18px; line-height:1.7;'>
<b>알쓸신잡은 언어의 또 다른 세계였고</b><br><br>
우리가 미처 쓰지 못했지만<br>
조금 다른 영역을 마주했던 이야기였고<br><br>
익숙한 것들 속에도<br>
새로운 시선과 놀라운 세계가 있다는 것을 느껴본 적 있는가?
</p>
""", unsafe_allow_html=True)

BASE_DIR = Path(__file__).resolve().parent.parent
html_path = BASE_DIR / "sub_geo_thm.html"

st.markdown("---")

with open(html_path, "r", encoding="utf-8") as f:
    html1 = f.read()

components.html(html1, height=1200, scrolling=True)

BASE_DIR = Path(__file__).resolve().parent.parent
html_path1 = BASE_DIR / "sub_seq.html"

st.markdown("---")

with open(html_path1, "r", encoding="utf-8") as f:
    html1 = f.read()

components.html(html1, height=1200, scrolling=True)
