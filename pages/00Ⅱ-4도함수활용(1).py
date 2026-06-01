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
# 슬라이드 1~2
for i in range(1, 3):
    st.image(
        f"assets/4 도함수활용(1)/images/슬라이드{i}.PNG",
        use_container_width=True
    )

# =========================

    with st.expander("🔍 MVT 확인하기", expanded=False):
        show_html(
        "assets/4 도함수활용(1)/html/mvt.html",
        height=600
    )




    st.image(
        "assets/4 도함수활용(1)/images/슬라이드3.PNG",
        use_container_width=True
    )

    
# =========================
# 중간 문구

st.markdown("""
<p style='font-size:18px; line-height:1.9;'>

겉으로 드러난 모양만을 보지 말라.<br>
<b> 참으로 살필 것은 그 안에서 일어나는 변화이니,</b><br>
찰나에 가까워질수록,<br>
도함수를 통하여 내적 변화를 읽어 보라.
</p>
""", unsafe_allow_html=True)

st.markdown("---")


# =========================
# 슬라이드 4~7
for i in range(4, 8):
    st.image(
        f"assets/4 도함수활용(1)/images/슬라이드{i}.PNG",
        use_container_width=True
    )
