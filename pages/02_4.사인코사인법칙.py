import streamlit as st
import streamlit.components.v1 as components

# 수정👉 외부 (URL)
url1 = "https://gemini.google.com/share/3ed7a18d47b2"
url2 = "https://gemini.google.com/share/fbe071558873"

# 제목 + 설명
st.title("🌌 탐구자들이여, 삼각형의 비밀을 밝혀라")
st.markdown("""
<p style='font-size:18px; font-weight:500; line-height:2; margin-bottom:10px;'>
세 변과 세 각 속에는, 눈에 보이지 않는 조화와 수학적 법칙이 흐르고 있습니다.
</p>

<p style='font-size:16px;'>
✔ 두 변과 끼인각 → <b>__법칙</b><br>
✔ 한 변과 두 각 → <b>__법칙</b>
</p>
""", unsafe_allow_html=True)

# 수정👉 내부 임베딩 (로컬 HTML)
with open("sincos.html", "r", encoding="utf-8") as f:
    html = f.read()
st.markdown("---")

components.html(html, height=950, scrolling=True)

# 수정 외부 url열기
st.link_button("👉전체 화면으로 보기", url1)

# 수정👉 내부 임베딩 (로컬 HTML)
with open("sincos_thm.html", "r", encoding="utf-8") as f:
    html = f.read()
st.markdown("---")    

# 수정👉 내부 임베딩 (로컬 HTML)
with open("geo_sub_thm.html", "r", encoding="utf-8") as f:
    html = f.read()
st.markdown("---")    
components.html(html, height=950, scrolling=True)
