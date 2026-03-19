import streamlit as st
import streamlit.components.v1 as components

# 수정👉 외부 (URL)
url1 = "https://gemini.google.com/share/5e531d00887d"

# 제목 + 설명
st.markdown("""
<p style='font-size:18px; line-height:1.7;'>
🌌 <b>알쓴신잡 : 수학의 또 다른 세계</b><br><br>
우리가 미처 알지 못했던<br>
조금 더 깊은 수학의 영역을 마주합니다.<br><br>
익숙한 것들 속에도<br>
새로운 시선과 놀라운 연결이 숨어 있습니다.
</p>
""", unsafe_allow_html=True)

# 수정👉 내부 임베딩 (로컬 HTML)
with open("geo_sub_thm.html", "r", encoding="utf-8") as f:
    html = f.read()
st.markdown("---")

components.html(html, height=950, scrolling=True)
