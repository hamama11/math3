import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 수정👉 외부 (URL)
url1 = "https://gemini.google.com/share/5e531d00887d"

# 제목 + 설명
st.markdown("""
<p style='font-size:18px; line-height:1.7;'>
😶‍🌫️ <b>알쓴신잡 : 00의 또 다른 세계</b><br><br>
우리가 미처 알지 못했던<br>
조금 다른 영역을 마주한적이<br><br>
익숙한 것들 속에도<br>
새로운 시선과 놀라운 세계가 있다는 것을 느껴본 적 있는가?
</p>
""", unsafe_allow_html=True)

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "geo_sub_thm.html", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=1400, scrolling=True)
