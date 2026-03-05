import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🧩 Root 근사 탐구")

URL = "https://hamama11.github.io/boostcamp/root근사.html"

st.markdown(
    f"""
⚠️ 만약 아래 화면이 보이지 않으면  
👉 [{URL}]({URL}) 로 직접 이동하세요.
"""
)

components.iframe(
    src=URL,
    width=1200,
    height=2200,
    scrolling=True
)
