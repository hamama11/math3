import streamlit as st
import streamlit.components.v1 as components

st.title("🧩 지수 Log 근사 추적")

st.markdown(
    """
    ⚠️ **만일 이 자리에서 화면이 드러나지 아니하거든,  
    아래에 적힌 바른 길을 밟아 곧장 나아가시옵소서.**  

    👉 [hamama11.github.io/boostcamp/limit.html](https://gemini.google.com/share/c534fffe3b24)

    **배움의 도(道)는 잠시 가려질지언정 끊어지지 아니하나니, 뜻을 세운 이라면 기필코 확인하여 탐구를 이어가시기 바라옵니다.**
    """,
    unsafe_allow_html=True
)

components.iframe(
    src="https://hamama11.github.io/boostcamp/limit.html",
    width=1200,
    height=2200,
    scrolling=True
)
