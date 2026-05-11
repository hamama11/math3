import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# 외부 URL
url1 = "https://gemini.google.com/share/3ed7a18d47b2"
url2 = "https://gemini.google.com/share/fbe071558873"

# 제목 + 설명
st.title("🌌 탐구자들이여, 삼각형의 비밀을 밝혀라")
st.markdown("""
<p style='font-size:18px; font-weight:500; line-height:2; margin-bottom:10px;'>
세 변과 세 각 속에는, 눈에 보이지 않는 조화와 수학적 법칙이 흐르고 있습니다.
</p>

<p style='font-size:16px;'>
✔ 두 변과 한 각 → <b>~~~법칙 </b> ✔ 한 변과 두 각 → <b>~~~법칙</b>
</p>
""", unsafe_allow_html=True)

# HTML 1
with open("cos_thm.html", "r", encoding="utf-8") as f:
    html1 = f.read()

wrapped_html1 = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html1}
</div>
"""

# HTML 2
with open("sin_thm.html", "r", encoding="utf-8") as f:
    html2 = f.read()

wrapped_html2 = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html2}
</div>
"""

tab1, tab2 = st.tabs(["코사인법칙", "사인법칙"])

with tab1:
    components.html(wrapped_html1, height=950, scrolling=True)
    st.link_button("👉 전체 화면으로 보기", url1, use_container_width=True)

with tab2:
    components.html(wrapped_html2, height=950, scrolling=True)
    st.link_button("👉 전체 화면으로 보기", url2, use_container_width=True)
