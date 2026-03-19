import streamlit as st
import streamlit.components.v1 as components

# 👉 GitHub Pages URL
url = "https://사용자명.github.io/레포명/assets/sine_cosine.html"

# 제목 + 설명
st.markdown("""
### 🌌 탐구자들이여, 삼각형의 비밀을 밝혀라

세 변과 세 각이 만들어내는 조화 속에는  
눈에 보이지 않는 수학적 법칙이 흐르고 있습니다.

✔ 두 변과 끼인각 → **코사인법칙**  
✔ 한 변과 두 각 → **사인법칙**

점을 움직이며 그 관계를 직접 추적해보세요.
""")

# 👉 외부 열기 버튼
st.link_button("🔗 새 탭에서 전체 화면으로 보기", url)
st.caption("💡 화면이 작으면 위 버튼을 눌러 전체 화면으로 보세요.")

st.markdown("---")

# 👉 내부 임베딩
components.html(
    f"""
    <iframe
        src="{url}"
        width="100%"
        height="700"
        style="border:none; border-radius:12px;">
    </iframe>
    """,
    height=720
)
