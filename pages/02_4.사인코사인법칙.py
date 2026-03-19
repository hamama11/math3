import streamlit as st
import streamlit.components.v1 as components

# 수정👉 외부 (URL)
url1 = "https://gemini.google.com/share/32e47da51ba9"
url2 = "https://gemini.google.com/share/fbe071558873"

# 제목 + 설명
st.title("🌌 탐구자들이여, 삼각형의 비밀을 밝혀라")
st.markdown("""
<p style='font-size:18px; font-weight:500; line-height:2; margin-bottom:10px;'>
세 변과 세 각 속에는, 눈에 보이지 않는 조화와 수학적 법칙이 흐르고 있습니다.
</p>

<p style='font-size:16px;'>
✔ 두 변과 끼인각 → <b>코사인법칙</b><br>
✔ 한 변과 두 각 → <b>사인법칙</b>
</p>
""", unsafe_allow_html=True)

# 외부 url열기
st.link_button("👉전체 화면으로 보기", url1)

# 수정👉 내부 임베딩 (로컬 HTML)
with open("sincos.html", "r", encoding="utf-8") as f:
    html = f.read()
st.markdown("---")

components.html(html, height=950, scrolling=True)

st.link_button("👉전체 화면으로 보기", url2)

# 수정👉 내부 임베딩 (로컬 HTML)
with open("sincos_thm.html", "r", encoding="utf-8") as f:
    html = f.read()
st.markdown("---")    
components.html(html, height=950, scrolling=True)
