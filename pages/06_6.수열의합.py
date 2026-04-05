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


# -------------------------------
# 🔢 ① 수열의 합과 귀납법
# -------------------------------
st.markdown(
    dedent("""
    <div style="display:flex; align-items:center; gap:12px; margin:10px 0; flex-wrap:wrap;">
        <h3 style="margin:0;">① 수열의 합과 귀납법</h3>
    </div>
    """),
    unsafe_allow_html=True
)

with open(BASE_DIR / "seq_sum.html", encoding="utf-8") as f:
    html1 = f.read()

components.html(html1, height=700, scrolling=True)

st.markdown("### ② 수열의 합과 대칭에 대한 의문")

with open(BASE_DIR / "seq_qes.html", encoding="utf-8") as f:
    html2 = f.read()

components.html(html2, height=700, scrolling=True)
