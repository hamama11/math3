import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="수열의 길",
    layout="wide"
)

# 현재 파일 기준 경로
BASE_DIR = Path(__file__).parent

# 외부 URL (필요 없으면 비워 두어도 됨)
url1 = ""
url2 = ""

# 제목 + 설명
st.title("🌌 탐구자들이여, 수의 흐름을 살피라")
st.markdown(
    """
    <p style='font-size:18px; font-weight:500; line-height:2; margin-bottom:10px;'>
    흐름을 살피노라면 마침내 숨은 이치가 드러나느니라.
    연이 닿거든 그 속에 인연을 지어 보자꾸나.
    </p>

    """,
    unsafe_allow_html=True
)

st.markdown("---")


def load_html(file_name: str):
    file_path = BASE_DIR / file_name
    if not file_path.exists():
        st.error(f"'{file_name}' 파일을 찾지 못하였소.")
        return None
    return file_path.read_text(encoding="utf-8")


# HTML 1
html1 = load_html("s_n,a_n.html")
if html1:
    wrapped_html1 = f"""
    <div style="width: 100%; margin: 0; padding: 0;">
        {html1}
    </div>
    """
    st.subheader("① 항과 합의 이치를 밝히다")
    components.html(wrapped_html1, height=700, scrolling=True)

st.markdown("")

# HTML 2
html2 = load_html("a_2n.html")
if html2:
    wrapped_html2 = f"""
    <div style="width: 100%; margin: 0; padding: 0;">
        {html2}
    </div>
    """
    st.subheader("② 부분은 전체를 보여주는가, 전체는 부분을 이야기하는가")
    components.html(wrapped_html2, height=700, scrolling=True)
