import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
from zoneinfo import ZoneInfo

st.set_page_config(page_title="Deepdive", page_icon="🌌", layout="wide")

# D-day (KST)
KST = ZoneInfo("Asia/Seoul")
today = datetime.now(KST).date()
target = date(2026, 11, 19)
d = (target - today).days
dday = f"D-{d}" if d > 0 else ("D-DAY" if d == 0 else f"D+{abs(d)}")

# Hero (우주+바다)
html = f"""
<!doctype html><html><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  html,body{{margin:0;padding:0}}
  .hero{{
    height:100vh; width:100%;
    display:flex; align-items:center; justify-content:center;
    position:relative; overflow:hidden;
    font-family:system-ui,-apple-system,Segoe UI,Roboto,"Noto Sans KR",sans-serif;
    background:
      radial-gradient(1200px 700px at 22% 26%, rgba(99,102,241,.35), transparent 60%),
      radial-gradient(900px 600px at 78% 72%, rgba(16,185,129,.18), transparent 62%),
      linear-gradient(160deg,#061026 0%,#0a1b3a 50%,#030714 100%);
  }}
  .milky{{
    position:absolute; inset:-40%;
    background:
      radial-gradient(closest-side at 50% 50%, rgba(255,255,255,.12), transparent 62%),
      conic-gradient(from 240deg, rgba(255,255,255,.06), rgba(99,102,241,.16),
        rgba(251,191,36,.10), rgba(16,185,129,.12), rgba(255,255,255,.06));
    filter: blur(70px);
    mix-blend-mode: screen;
    opacity:.85;
    animation: drift 12s linear infinite;
  }}
  @keyframes drift{{0%{{transform:translate(-6%,-4%) rotate(0) scale(1.05)}}
    50%{{transform:translate(6%,5%) rotate(180deg) scale(1.10)}}
    100%{{transform:translate(-6%,-4%) rotate(360deg) scale(1.05)}}}}
  .stars{{
    position:absolute; inset:0; opacity:.85;
    background:
      radial-gradient(circle at 8% 18%, rgba(255,255,255,.95) 0 1px, transparent 2px),
      radial-gradient(circle at 16% 62%, rgba(255,255,255,.80) 0 1px, transparent 2px),
      radial-gradient(circle at 28% 30%, rgba(255,255,255,.65) 0 1px, transparent 2px),
      radial-gradient(circle at 42% 16%, rgba(255,255,255,.75) 0 1px, transparent 2px),
      radial-gradient(circle at 55% 40%, rgba(255,255,255,.60) 0 1px, transparent 2px),
      radial-gradient(circle at 68% 22%, rgba(255,255,255,.70) 0 1px, transparent 2px),
      radial-gradient(circle at 76% 52%, rgba(255,255,255,.58) 0 1px, transparent 2px),
      radial-gradient(circle at 88% 26%, rgba(255,255,255,.65) 0 1px, transparent 2px);
    animation: twinkle 3s ease-in-out infinite alternate;
  }}
  @keyframes twinkle{{from{{opacity:.45}}to{{opacity:.95}}}}
  .ocean{{
    position:absolute; left:0; right:0; bottom:0; height:46vh;
    background:
      radial-gradient(1000px 260px at 26% 40%, rgba(59,130,246,.28), transparent 65%),
      radial-gradient(800px 240px at 78% 70%, rgba(16,185,129,.16), transparent 65%),
      linear-gradient(180deg, rgba(2,6,23,0) 0%, rgba(2,6,23,.30) 18%, rgba(2,6,23,.92) 100%);
  }}
  .wave{{
    position:absolute; left:-25%; width:150%;
    height:64px; bottom:13vh;
    background:rgba(255,255,255,.055); border-radius:999px;
    animation: wave 8s ease-in-out infinite;
  }}
  .wave.w2{{bottom:9vh;height:52px;opacity:.7;animation-duration:10s;animation-direction:reverse}}
  .wave.w3{{bottom:5vh;height:44px;opacity:.55;animation-duration:12s}}
  @keyframes wave{{0%{{transform:translateX(0) scaleY(1)}}
    50%{{transform:translateX(6%) scaleY(1.16)}}100%{{transform:translateX(0) scaleY(1)}}}}
  .center{{
    position:relative; z-index:2;
    text-align:center; padding:24px;
  }}
  .title{{
    font-weight:1000; letter-spacing:-1px; line-height:1.05;
    font-size:min(7vw,56px);
    color:rgba(255,255,255,.92);
    text-shadow:0 18px 60px rgba(0,0,0,.55);
  }}
  .dday{{
    margin-top:14px;
    font-weight:1000; line-height:1;
    font-size:min(16vw,150px);
    background:linear-gradient(135deg, rgba(251,191,36,1), rgba(99,102,241,1), rgba(16,185,129,1));
    -webkit-background-clip:text; background-clip:text; color:transparent;
    filter:drop-shadow(0 16px 32px rgba(99,102,241,.25));
  }}
  .sub{{
    margin-top:10px;
    font-weight:850;
    color:rgba(199,210,254,.9);
    font-size:min(4vw,22px);
  }}
  .chip{{
    margin-top:10px; display:inline-block;
    padding:8px 12px; border-radius:999px;
    border:1px solid rgba(255,255,255,.14);
    background:rgba(2,6,23,.30);
    color:rgba(255,255,255,.78);
    font-weight:800; font-size:13px;
  }}
</style></head>
<body>
  <div class="hero">
    <div class="milky"></div>
    <div class="stars"></div>
    <div class="ocean">
      <div class="wave"></div><div class="wave w2"></div><div class="wave w3"></div>
    </div>

    <div class="center">
      <div class="title">Deepdive</div>
      <div class="dday">{dday}</div>
      <div class="sub">2026-11-19 · KST</div>
      <div class="chip">우주 × 바다 · 아래 버튼으로 이동</div>
    </div>
  </div>
</body></html>
"""
components.html(html, height=900, scrolling=False)

# ✅ 중하단 버튼(스트림릿 버튼이 더 안정적)
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.page_link("pages/01_1.지수log.py", label="🚀 지수·로그 Deepdive로 들어가기", use_container_width=True)
