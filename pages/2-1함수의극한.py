import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.image(
    "assets/함수의극한/images/슬라이드3.png",
    use_container_width=True
)

with open(
    "assets/함수의극한/html/4번.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

components.html(html, height=950, scrolling=True)

st.image(
    "assets/함수의극한/images/슬라이드4.png",
    use_container_width=True
)
