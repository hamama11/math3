import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
from zoneinfo import ZoneInfo

st.set_page_config(page_title="Deepdive", page_icon="🌌", layout="wide")

# D-day (KST)
KST = ZoneInfo("Asia/Seoul")
d = (date(2026, 11, 19) - datetime.now(KST).date()).days
dday = f"D-{d}" if d > 0 else ("D-DAY" if d == 0 else f"D+{abs(d)}")

# 홈 HTML 로드
with open("home.html", "r", encoding="utf-8") as f:
    html = f.read().replace("{{DDAY}}", dday)

# ✅ 홈 화면 (D-day 아래에 spacer가 있으니 높이 충분히)
components.html(html, height=600, scrolling=False)

# ✅ 버튼(페이지 링크) 텍스트 중앙 정렬 CSS
st.markdown("""
<style>
/* page_link가 버튼으로 렌더될 때 텍스트 중앙 정렬 */
a[data-testid="stPageLink-NavLink"], a[data-testid="stPageLink-NavLink"] * {
  justify-content: center !important;
  text-align: center !important;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    b1, b2, b3, b4 = st.columns(3)

    with b1:
        if st.button("🔄️ 지수·로그", use_container_width=True):
            st.switch_page("pages/01_1.지수log.py")
    with b2:
        if st.button("📐 사인·코사인법칙", use_container_width=True):
            st.switch_page("pages/02_4.사인코사인법칙.py")
    with b3:
        if st.button("🔢 수열", use_container_width=True):
            st.switch_page("pages/03_5.등차등비수열.py")
    with b4:
        if st.button("😶‍🌫️ 알쓴신잡 ", use_container_width=True):
            st.switch_page("pages/알쓴신잡.py")

