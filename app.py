import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
from zoneinfo import ZoneInfo

st.set_page_config(page_title="Deepdive", page_icon="🌌", layout="wide")

KST = ZoneInfo("Asia/Seoul")
d = (date(2026, 11, 19) - datetime.now(KST).date()).days
dday = f"D-{d}" if d > 0 else ("D-DAY" if d == 0 else f"D+{abs(d)}")

with open("home.html", "r", encoding="utf-8") as f:
    html = f.read().replace("{{DDAY}}", dday)

components.html(html, height=500, scrolling=False)  # ✅ 여기 숫자만 미세조정

# ✅ HTML 바로 밑: 이동 버튼
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.page_link("pages/01_1.지수log.py", label="🚀 지수·로그로 이동", use_container_width=True)
