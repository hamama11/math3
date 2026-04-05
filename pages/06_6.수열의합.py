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
    수는 쌓이며 흐름을 이루고,<br>
    그 흐름은 스스로 법도를 만들기도 한다.<br><br>

    하나를 딛고 다음을 나아가며,<br>
    끝내 모든 것을 밝혀내는 길,<br><br>

    우리가 살아가는 모습과도 닮아 있지 않겠는가.
    그대는 이미 흐름을 꿰뚫는 자이니라.<br>
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

with open(BASE_DIR / "6.seq_sum.html", encoding="utf-8") as f:
    html1 = f.read()

components.html(html1, height=800, scrolling=True)

st.markdown("### ② 수열의 합과 대칭에 대한 의문")

with open(BASE_DIR / "6.seq_qes.html", encoding="utf-8") as f:
    html2 = f.read()

components.html(html2, height=1000, scrolling=True)
