import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# =========================
# 슬라이드 1~7
# =========================

for i in range(1, 8):
    st.image(
        f"assets/4 도함수활용(1)/images/슬라이드{i}.PNG",
        use_container_width=True
    )



# =========================
# 2종 예시 HTML
# =========================

show_html(
    "assets/미분계수와도함수/html/2종예시.html",
    title="f'(x) 불연속 예시🔍",
    height=600
)

left, right = st.columns([1, 1])

with left:
    st.image(
        "assets/미분계수와도함수/images/슬라이드6.PNG",
         use_container_width=True
    )
with right:
    show_html(
        "assets/미분계수와도함수/html/2종불연속3D.html",
         height=900
    )
