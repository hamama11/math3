import streamlit as st
import streamlit.components.v1 as components


st.title("🧩 Root 제곱근/세제곱근 근사 추적", layout="wide")

PAGES_URL = "https://hamama11.github.io/math3/newton.html"  # ✅ 여기만 바꾸면 됨

st.markdown(
    f"""
    ⚠️ **만일 이 자리에서 화면이 드러나지 아니하거든, 아래의 길로 곧장 나아가시옵소서.**  
    👉 [{PAGES_URL}]({PAGES_URL})

    **배움의 도(道)는 잠시 가려질지언정 끊어지지 아니하나니, 뜻을 세운 이라면 기필코 확인하여 탐구를 이어가시기 바라옵니다.**
    """,
    unsafe_allow_html=True
)

components.iframe(
    src=PAGES_URL,
    width=1200,
    height=2200,
    scrolling=True
)
