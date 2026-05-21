import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

left, right = st.columns([1.3, 1])

with left:
    st.image(
        "assets/미분계수와도함수/images/슬라이드1.PNG",
        use_container_width=True
    )
    
with right:
    st.markdown("""
    <p style='font-size:19px; line-height:2;'>

    🌌 <b>변화</b>

    우리는 매 순간 달라지고 흔들리건만,<br>
    어째서 여전히 같은 사람이라 말하는 것이더냐.<br><br>

    하루의 변화는 너무 작아 보이기에 스스로도 깨닫지 못하나,<br>
    어느새 사람의 생각과 마음, 삶의 방향까지 바꾸어 놓기도 하도다.<br><br>
    
    두 순간 사이의 거대한 차이를 보는 것이 아니라<br>
    <b>‘지금 이 순간, 나는 어떤 방향으로 변하고 있는가’</b><br><br>
    
    두려움은 변화 그 자체가 아니라,<br>
    변화하고 있음에도 스스로 어디로 향하는지 잊어버리는 일인지도 모르도다.<br><br>
    </p>
    """, unsafe_allow_html=True)

# 좌우 배치
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

# HTML 불러오기
html_path = "assets/미분계수와도함수/html/미분계수.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

wrapped_html = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html_content}
</div>
"""

with st.expander("🔍 <span style='font-size:24px;'>lim f'(x) ≠ f'(x)</span>",expanded=False):
    components.html(
        wrapped_html,
        height=900,
        scrolling=True
    )

st.markdown("---")

st.markdown("""
<p style='font-size:18px; line-height:1.9;'>

🔍 <b>가까워질수록 더 선명해지는 것이 있도다.</b><br><br>

찰나에 가까워질수록,<br>
우리는 비로소 변화의 진짜 방향을 마주하게 되도다.

</p>
""", unsafe_allow_html=True)

st.markdown("---")

# 🖼 슬라이드 3~5
for i in range(3, 6):
    st.image(
        f"assets/미분계수와도함수/images/슬라이드{i}.PNG",
        use_container_width=True
    )


# HTML 불러오기
html_path = "assets/미분계수와도함수/html/2종불연속.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

wrapped_html = f"""
<div style="width: 100%; margin: 0; padding: 0;">
    {html_content}
</div>
"""
import streamlit as st

with st.expander("🔍 f(x)=x²sin(1/x) 에서 f'(0)은 연속일까?", expanded=False):

    st.markdown("""
    <p style='font-size:18px; line-height:1.9;'>

    함수 \\( f(x) \\)를 다음과 같이 정의하자.

    </p>
    """, unsafe_allow_html=True)

    st.latex(r"""
    f(x)=
    \begin{cases}
    x^2\sin\frac{1}{x}, & x\neq 0 \\
    0, & x=0
    \end{cases}
    """)

    st.markdown("""
    <p style='font-size:18px; line-height:1.9;'>

    먼저 \\(x=0\\)에서의 미분계수를 정의로 계산하면,

    </p>
    """, unsafe_allow_html=True)

    st.latex(r"""
    f'(0)
    =
    \lim_{h\to 0}\frac{f(h)-f(0)}{h}
    =
    \lim_{h\to 0}\frac{h^2\sin(1/h)}{h}
    =
    \lim_{h\to 0}h\sin(1/h)
    """)

    st.markdown("""
    <p style='font-size:18px; line-height:1.9;'>

    이때 \\(-|h| \\le h\\sin(1/h) \\le |h|\\) 이므로 샌드위치 정리에 의해,

    </p>
    """, unsafe_allow_html=True)

    st.latex(r"""
    \lim_{h\to 0}h\sin(1/h)=0
    """)

    st.latex(r"""
    \therefore f'(0)=0
    """)

    st.markdown("""
    <p style='font-size:18px; line-height:1.9;'>

    이제 \\(x\\neq 0\\)에서 도함수를 구하면,

    </p>
    """, unsafe_allow_html=True)

    st.latex(r"""
    f'(x)
    =
    2x\sin\frac{1}{x}
    +
    x^2\cos\frac{1}{x}\cdot\left(-\frac{1}{x^2}\right)
    """)

    st.latex(r"""
    f'(x)
    =
    2x\sin\frac{1}{x}
    -
    \cos\frac{1}{x}
    \quad (x\neq 0)
    """)

    st.markdown("""
    <p style='font-size:18px; line-height:1.9;'>

    여기서 \\(x\\to 0\\)일 때 첫 번째 항은

    </p>
    """, unsafe_allow_html=True)

    st.latex(r"""
    2x\sin\frac{1}{x}\to 0
    """)

    st.markdown("""
    <p style='font-size:18px; line-height:1.9;'>

    하지만 두 번째 항 \\(-\\cos(1/x)\\)는 \\(x\\to 0\\)에서 계속 진동하므로 극한이 존재하지 않는다.

    </p>
    """, unsafe_allow_html=True)

    st.latex(r"""
    \lim_{x\to 0}f'(x)
    =
    \lim_{x\to 0}
    \left(
    2x\sin\frac{1}{x}
    -
    \cos\frac{1}{x}
    \right)
    \quad \text{does not exist}
    """)

    st.markdown("""
    <p style='font-size:18px; line-height:1.9;'>

    따라서 \\(f'(0)\\)은 존재하지만,<br>
    \\(\\lim_{x\\to 0}f'(x)\\)는 존재하지 않는다.

    </p>
    """, unsafe_allow_html=True)

    st.latex(r"""
    f'(0)=0
    \quad \text{but} \quad
    \lim_{x\to 0}f'(x) \text{ does not exist}
    """)

    st.markdown("""
    <p style='font-size:18px; line-height:1.9;'>

    그러므로 도함수 \\(f'\\)는 \\(x=0\\)에서 연속이 아니다.

    </p>
    """, unsafe_allow_html=True)

    st.latex(r"""
    \therefore f'(x)\text{ is not continuous at }x=0
    """)

with st.expander("</b>🔍lim f' != f'", expanded=False):
    components.html(
        wrapped_html,
        height=900,
        scrolling=True
    )
