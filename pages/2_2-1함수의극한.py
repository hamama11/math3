import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# 🌌 제목
st.title("🌊 함수의 극한 : 미시와 거시의 시선")

# ✨ 설명
st.markdown("""
<p style='font-size:18px; font-weight:500; line-height:2; margin-bottom:10px;'>
함수의 극한은 한 점을 향해 아주 가까이 다가가는 <b>미시적 관찰</b>에서 시작됩니다.<br>
그러나 그 작은 움직임을 따라가다 보면, 그래프 전체의 흐름과 구조를 바라보는 <b>거시적 이해</b>로 이어집니다.
</p>

<p style='font-size:16px; line-height:1.8;'>
✔ 미시적 시선 → 점 근처에서 함수값이 어떻게 움직이는가<br>
✔ 거시적 시선 → 그래프 전체의 흐름 속에서 어떤 값으로 향하는가
</p>
""", unsafe_allow_html=True)

# =========================
# 🖼 슬라이드 1 ~ 3
# =========================

for i in range(1, 4):
    st.image(
        f"assets/함수의극한/images/슬라이드{i}.PNG",
        use_container_width=True
    )

# =========================
# 🌐 HTML 인터랙션
# =========================

with open(
    "assets/함수의극한/html/p14_lv2_4번.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

wrapped_html = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html}
</div>
"""

st.markdown("---")

components.html(
    wrapped_html,
    height=950,
    scrolling=True
)

# =========================
# 🖼 슬라이드 5 ~ 6
# =========================

for i in range(5, 7):
    st.image(
        f"assets/함수의극한/images/슬라이드{i}.PNG",
        use_container_width=True
    )
