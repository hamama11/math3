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
# 슬라이드 1
st.image(
    "assets/5 도함수활용(2)/images/슬라이드1.PNG",
    use_container_width=True
)

# =========================
# 슬라이드 2 + HTML
with st.expander("🔍 합성함수그래프", expanded=False):
        show_html(
            "assets/5 도함수활용(2)/html/합성함수그래프개형.html",
            height=650
        )
     st.markdown(
            "[새 창에서 열기](https://gemini.google.com/share/d7b63f6e840e)"
        )
    
st.image(
        "assets/5 도함수활용(2)/images/슬라이드2.PNG",
        use_container_width=True
    )

# =========================
# 슬라이드 3~6
for i in range(3, 7):
    st.image(
        f"assets/5 도함수활용(2)/images/슬라이드{i}.PNG",
        use_container_width=True
    )

# =========================
# 중간 문구
st.markdown("""
<p style='font-size:18px; line-height:1.9;'>

겉으로 드러난 모양만을 보지 말라.<br>
<b>참으로 살필 것은 그 안에서 일어나는 변화이니,</b><br>
찰나에 가까워질수록,<br>
도함수를 통하여 내적 변화를 읽어 보라.
</p>
""", unsafe_allow_html=True)

st.markdown("---")


# =========================
# 슬라이드 7 + 지오지브라

st.image(
        "assets/5 도함수활용(2)/images/슬라이드7.PNG",
        use_container_width=True
    )


with st.expander("📌 지오지브라 열기", expanded=False):
        components.iframe(
            src="https://www.geogebra.org/calculator/vmv32qkk",
            height=650,
            scrolling=True
        )

        st.markdown(
            "[새 창에서 열기](https://www.geogebra.org/calculator/vmv32qkk)"
        )


# =========================
# 슬라이드 8
st.image(
    "assets/5 도함수활용(2)/images/슬라이드8.PNG",
    use_container_width=True
)
