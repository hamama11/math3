import streamlit as st
import streamlit.components.v1 as components

st.markdown("""
### 🌌 탐구자들이여, 삼각형의 비밀을 밝혀라

세 변과 세 각이 만들어내는 조화 속에는  
눈에 보이지 않는 수학적 법칙이 흐르고 있습니다.

✔ 두 변과 끼인각 → 코사인법칙  
✔ 한 변과 두 각 → 사인법칙  
""")

components.html(
    """
    <iframe
        src="https://사용자명.github.io/레포명/assets/sine_cosine.html"
        width="100%"
        height="700"
        style="border:none; border-radius:12px;">
    </iframe>
    """,
    height=720
)
