import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")


# =========================
# HTML 출력 함수
def show_html(path, title=None, height=600):
    if title:
        st.subheader(title)

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    components.html(html, height=height, scrolling=True)


# =========================
# 슬라이드 1~3
for i in range(1, 4):
    st.image(
        f"assets/4 도함수활용(1)/images/슬라이드{i}.PNG",
        use_container_width=True
    )


# =========================
# HTML
show_html(
    "assets/4 도함수활용(1)/html/mvt.html",
    title="MVT",
    height=600
)


# =========================
# 슬라이드 4~7
for i in range(4, 8):
    st.image(
        f"assets/4 도함수활용(1)/images/슬라이드{i}.PNG",
        use_container_width=True
    )
