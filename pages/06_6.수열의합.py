import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from textwrap import dedent

st.set_page_config(layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent

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

st.markdown(
    dedent("""
    <div style="display:flex; align-items:center; gap:12px; margin:10px 0;">
        <h3 style="margin:0;">① 수열의 흐름을 따라</h3>
        <a href="https://gemini.google.com/share/461584169a61" target="_blank"
           style="font-size:14px; text-decoration:none; padding:7px 14px; border-radius:999px; background:#111; color:white;">
           👉전체 화면으로 보기 click
        </a>
    </div>
    """),
    unsafe_allow_html=True
)

with open(BASE_DIR / "seq_sum.html", encoding="utf-8") as f:
    html1 = f.read()

components.html(html1, height=700, scrolling=True)

