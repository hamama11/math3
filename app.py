import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
from zoneinfo import ZoneInfo

st.set_page_config(page_title="SM 수학사무소", layout="wide")

# D-day
KST = ZoneInfo("Asia/Seoul")
today = datetime.now(KST).date()
target = date(2026, 11, 19)
d = (target - today).days
dday = f"D-{d}" if d > 0 else ("D-DAY" if d == 0 else f"D+{abs(d)}")

# 홈(애니메이션/대문) — HTML은 별도 파일로 분리해서 짧게 로드
with open("assets/home.html", "r", encoding="utf-8") as f:
    html = f.read().replace("{{DDAY}}", dday)

components.html(html, height=900, scrolling=False)

# ✅ 홈 -> 페이지 (사이드바)
with st.sidebar:
    st.markdown("### 📄 Pages")
    st.page_link("pages/01.지수log.py", label="📘 지수·로그", use_container_width=True)
