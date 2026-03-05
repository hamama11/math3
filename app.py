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
components.html(html, height=900, scrolling=False)

# ✅ 홈(HTML) 바로 아래: 이동 버튼
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.page_link("pages/01.지수log.py", label="🚀 지수·로그 Deepdive로 이동", use_container_width=True)
