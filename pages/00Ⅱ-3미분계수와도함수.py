import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")


# =========================
# 공통 함수
# =========================

def show_html(path, title="🔍 인터랙션", height=900):
    with open(path, "r", encoding="utf-8") as f:
        html_content = f.read()

    wrapped_html = f"""
    <div style="width: 100%; margin: 0; padding: 0;">
        {html_content}
    </div>
    """

    with st.expander(title, expanded=False):
        components.html(
            wrapped_html,
            height=height,
            scrolling=True
        )


# =========================
# 슬라이드 1 + 머리말
# =========================

left, right = st.columns([1.3, 1])

with left:
    st.image(
        "assets/미분계수와도함수/images/슬라이드1.PNG",
        use_container_width=True
    )

with right:
    st.markdown("""
    <p style='font-size:19px; line-height:2;'>

    🌌 <b>변화</b><br><br>

    우리는 매 순간 달라지고 흔들리건만,<br>
    어째서 여전히 같은 사람이라 말하는 것이더냐.<br><br>

    하루의 변화는 너무 작아 보이기에 스스로도 깨닫지 못하나,<br>
    어느새 사람의 생각과 마음, 삶의 방향까지 바꾸어 놓기도 하도다.<br><br>
    
    두 순간 사이의 거대한 차이를 보는 것이 아니라<br>
    <b>‘지금 이 순간, 나는 어떤 방향으로 변하고 있는가’</b><br><br>
    
    두려움은 변화 그 자체가 아니라,<br>
    변화하고 있음에도 스스로 어디로 향하는지 잊어버리는 일인지도 모르도다.

    </p>
    """, unsafe_allow_html=True)


st.markdown("---")


# =========================
# 슬라이드 2 + 풀이 이미지
# =========================

left, right = st.columns([1, 1.2])

with left:
    st.image(
        "assets/미분계수와도함수/images/슬라이드2.PNG",
        use_container_width=True
    )

with right:
    with st.expander("🔍 풀이", expanded=False):
        st.image(
            "assets/미분계수와도함수/images/슬라이드2-3.PNG",
            use_container_width=True
        )


# =========================
# 미분계수 Quiz HTML
# =========================

show_html(
    "assets/미분계수와도함수/html/미분계수.html",
    title="🔍 미분계수 Quiz",
    height=900
)

# =========================
# 중간 문구
# =========================

st.markdown("""
<p style='font-size:18px; line-height:1.9;'>

🔍 <b>가까워질수록 더 선명해지는 것이 있도다.</b><br><br>

찰나에 가까워질수록,<br>
우리는 비로소 변화의 진짜 방향을 마주하게 되도다.

</p>
""", unsafe_allow_html=True)


st.markdown("---")


# =========================
# 슬라이드 3~5
# =========================

for i in range(3, 6):
    st.image(
        f"assets/미분계수와도함수/images/슬라이드{i}.PNG",
        use_container_width=True
    )


# =========================
# 2종 불연속 HTML
# =========================

show_html(
    "assets/미분계수와도함수/html/2종불연속.html",
    title="Graph🔍 속도가 불연속??? limf'(a)=f'(a)?",
    height=800
)


# =========================
# 2종 예시 HTML
# =========================

show_html(
    "assets/미분계수와도함수/html/2종예시.html",
    title="3D🔍",
    height=600
)

left, right = st.columns([1, 1])

with left:
    st.image(
        "assets/미분계수와도함수/images/슬라이드6.PNG",
         height=600
    )
with right:
    show_html(
        "assets/미분계수와도함수/html/2종불연속3D.html",
        use_container_width=True
    )
