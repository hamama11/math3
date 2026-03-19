import streamlit as st
import streamlit.components.v1 as components

# 👉 외부 URL (A)
url = "https://gemini.google.com/share/6a5009e17e54"

# 제목 + 설명
st.markdown("""
### 🌌 탐구자들이여, 삼각형의 비밀을 밝혀라
세 변과 세 각 속에는 눈에 보이지 않는 조화와 수학적 법칙이 흐르고 있습니다.
<span style='font-size:18px; font-weight:500;'>
</span>

✔ 두 변과 끼인각 → **코사인법칙**  
✔ 한 변과 두 각 → **사인법칙**

""")

# 👉 외부 열기 (A 사용)
st.link_button("👉전체 화면으로 보기", url)

st.markdown("---")
# 👉 내부 임베딩 (로컬 HTML)
with open("sincos.html", "r", encoding="utf-8") as f:
    html = f.read()
    
components.html(html, height=950, scrolling=True)
