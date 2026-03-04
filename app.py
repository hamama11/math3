import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="SM 수학사무소", layout="wide")

html_path = Path(__file__).parent / "page.html"
html = html_path.read_text(encoding="utf-8")

# HTML 내부의 상대경로(assets/...)가 동작하도록 base URL 느낌을 맞추긴 어렵지만,
# streamlit cloud에선 보통 아래 방식으로도 잘 뜹니다.
components.html(html, height=2400, scrolling=True)
