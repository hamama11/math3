import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
from zoneinfo import ZoneInfo

st.set_page_config(page_title="SM 수학사무소", layout="wide")

KST = ZoneInfo("Asia/Seoul")
today = datetime.now(KST).date()
target = date(2026, 11, 19)
dday = (target - today).days
dday_label = f"D-{dday}" if dday > 0 else ("D-DAY" if dday == 0 else f"D+{abs(dday)}")

# pages (현재 1개)
PAGE_URL = "?page=pages/1.%EC%A7%80%EC%88%98log"  # Streamlit multipage 내부 라우팅(환경마다 다를 수 있어 fallback도 같이 둠)

html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<style>
  html, body {{ margin:0; padding:0; height:100%; }}
  .hero {{
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    background:
      radial-gradient(1200px 700px at 25% 30%, rgba(99,102,241,0.30), transparent 60%),
      radial-gradient(900px 600px at 82% 72%, rgba(16,185,129,0.18), transparent 62%),
      linear-gradient(160deg, #07102a 0%, #0b1a36 48%, #050a18 100%);
    font-family: system-ui, -apple-system, Segoe UI, Roboto, "Noto Sans KR", sans-serif;
  }}

  .milkyway {{
    position:absolute; inset:-45%;
    background:
      radial-gradient(closest-side at 50% 50%, rgba(255,255,255,0.14), transparent 62%),
      conic-gradient(from 240deg,
        rgba(255,255,255,0.08),
        rgba(99,102,241,0.16),
        rgba(251,191,36,0.10),
        rgba(16,185,129,0.12),
        rgba(255,255,255,0.08)
      );
    filter: blur(65px);
    opacity: 0.80;
    animation: drift 11s linear infinite;
    mix-blend-mode: screen;
  }}
  @keyframes drift {{
    0%   {{ transform: translate3d(-6%, -4%, 0) rotate(0deg) scale(1.05); }}
    50%  {{ transform: translate3d( 6%,  5%, 0) rotate(180deg) scale(1.10); }}
    100% {{ transform: translate3d(-6%, -4%, 0) rotate(360deg) scale(1.05); }}
  }}

  .stars {{
    position:absolute; inset:0;
    opacity: 0.85;
    background:
      radial-gradient(circle at 6% 14%, rgba(255,255,255,0.95) 0 1px, transparent 2px),
      radial-gradient(circle at 12% 44%, rgba(255,255,255,0.80) 0 1px, transparent 2px),
      radial-gradient(circle at 18% 72%, rgba(255,255,255,0.70) 0 1px, transparent 2px),
      radial-gradient(circle at 26% 28%, rgba(255,255,255,0.65) 0 1px, transparent 2px),
      radial-gradient(circle at 34% 56%, rgba(255,255,255,0.55) 0 1px, transparent 2px),
      radial-gradient(circle at 42% 16%, rgba(255,255,255,0.75) 0 1px, transparent 2px),
      radial-gradient(circle at 50% 40%, rgba(255,255,255,0.60) 0 1px, transparent 2px),
      radial-gradient(circle at 58% 70%, rgba(255,255,255,0.50) 0 1px, transparent 2px),
      radial-gradient(circle at 66% 22%, rgba(255,255,255,0.70) 0 1px, transparent 2px),
      radial-gradient(circle at 74% 48%, rgba(255,255,255,0.58) 0 1px, transparent 2px),
      radial-gradient(circle at 82% 18%, rgba(255,255,255,0.65) 0 1px, transparent 2px),
      radial-gradient(circle at 90% 64%, rgba(255,255,255,0.55) 0 1px, transparent 2px);
    animation: twinkle 3s ease-in-out infinite alternate;
  }}
  @keyframes twinkle {{
    from {{ opacity: 0.45; }}
    to   {{ opacity: 0.95; }}
  }}

  .ocean {{
    position:absolute; left:0; right:0; bottom:0;
    height: 46vh;
    background:
      radial-gradient(1000px 260px at 28% 40%, rgba(59,130,246,0.26), transparent 65%),
      radial-gradient(800px 240px at 82% 70%, rgba(16,185,129,0.16), transparent 65%),
      linear-gradient(180deg, rgba(2,6,23,0) 0%, rgba(2,6,23,0.30) 18%, rgba(2,6,23,0.90) 100%);
  }}

  .wave {{
    position:absolute; left:-25%; width:150%;
    height: 70px; bottom: 14vh;
    background: rgba(255,255,255,0.055);
    border-radius: 999px;
    animation: wave 7s ease-in-out infinite;
  }}
  .wave.w2 {{ bottom: 10vh; height: 56px; opacity: 0.70; animation-duration: 9s; animation-direction: reverse; }}
  .wave.w3 {{ bottom:  6vh; height: 48px; opacity: 0.55; animation-duration: 11s; }}
  @keyframes wave {{
    0%   {{ transform: translateX(0%)   scaleY(1); }}
    50%  {{ transform: translateX(6%)   scaleY(1.18); }}
    100% {{ transform: translateX(0%)   scaleY(1); }}
  }}

  .center {{
    position:absolute; inset:0;
    display:flex; align-items:center; justify-content:center;
    text-align:center;
    padding: 24px;
    pointer-events: none;
  }}
  .dday {{
    font-weight: 1000;
    letter-spacing: -1.2px;
    line-height: 1.0;
    text-shadow: 0 18px 60px rgba(0,0,0,0.55);
  }}
  .dday .big {{
    font-size: min(16vw, 150px);
    background: linear-gradient(135deg, rgba(251,191,36,1), rgba(99,102,241,1), rgba(16,185,129,1));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    filter: drop-shadow(0 16px 32px rgba(99,102,241,0.25));
  }}
  .dday .sub {{
    margin-top: 10px;
    font-size: min(4.2vw, 28px);
    font-weight: 900;
    color: rgba(199,210,254,0.95);
  }}
  .dday .date {{
    margin-top: 6px;
    font-size: min(3.2vw, 18px);
    font-weight: 800;
    color: rgba(255,255,255,0.65);
  }}
  .dday .deep {{
    margin-top: 14px;
    display:inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(2,6,23,0.28);
    font-size: 14px;
    font-weight: 900;
    color: rgba(255,255,255,0.80);
  }}

  /* 유영 생물 */
  .swim {{
    position:absolute;
    left:-22%;
    bottom:16vh;
    font-size:46px;
    opacity:0.95;
    animation: swim 18s linear infinite, bob 2.6s ease-in-out infinite;
    filter: drop-shadow(0 10px 30px rgba(0,0,0,0.45));
    user-select:none;
  }}
  .swim.whale1 {{ bottom:19vh; font-size:58px; animation-duration: 24s; }}
  .swim.turtle {{ bottom:12vh; font-size:46px; animation-duration: 20s; }}
  .swim.whale2 {{ bottom: 8vh; font-size:50px; animation-duration: 28s; opacity:0.78; }}

  .swim.manta {{
    bottom: 14vh;
    width: 92px;
    height: 62px;
    font-size: 0;
    opacity: 0.88;
    animation-duration: 23s;
  }}
  .swim.manta svg {{ width:100%; height:100%; }}

  @keyframes swim {{ 0%{{ transform: translateX(0vw); }} 100%{{ transform: translateX(145vw); }} }}
  @keyframes bob  {{ 0%,100%{{ transform: translateY(0px); }} 50%{{ transform: translateY(-10px); }} }}

  /* 하단 이동 버튼(HTML 버튼) */
  .nav {{
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    bottom: 18px;
    z-index: 9999;
    display:flex;
    gap: 10px;
    padding: 10px 12px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(2,6,23,0.45);
    backdrop-filter: blur(12px);
    box-shadow: 0 18px 60px rgba(0,0,0,0.35);
    pointer-events: auto;
  }}
  .nav a {{
    text-decoration:none;
    padding: 10px 14px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(255,255,255,0.06);
    color: rgba(255,255,255,0.92);
    font-weight: 900;
    font-size: 14px;
  }}
  .nav a:hover {{
    background: rgba(255,255,255,0.10);
  }}

  .hint {{
    position:absolute;
    left:50%;
    transform: translateX(-50%);
    bottom: 72px;
    font-size: 13px;
    font-weight: 850;
    color: rgba(255,255,255,0.62);
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(2,6,23,0.32);
    border: 1px solid rgba(255,255,255,0.10);
    backdrop-filter: blur(10px);
  }}
</style>
</head>
<body>
  <div class="hero">
    <div class="milkyway"></div>
    <div class="stars"></div>

    <div class="ocean">
      <div class="wave"></div>
      <div class="wave w2"></div>
      <div class="wave w3"></div>

      <div class="swim turtle">🐢</div>
      <div class="swim whale1">🐋</div>
      <div class="swim whale2">🐋</div>

      <div class="swim manta" aria-label="manta">
        <svg viewBox="0 0 220 140" xmlns="http://www.w3.org/2000/svg">
          <path d="M110 20 C75 22 40 45 22 78 C10 100 22 122 48 114
                   C70 108 88 90 110 90 C132 90 150 108 172 114
                   C198 122 210 100 198 78 C180 45 145 22 110 20Z"
                fill="rgba(255,255,255,0.18)"/>
          <path d="M110 90 C104 104 98 115 86 126 C102 120 108 112 110 104
                   C112 112 118 120 134 126 C122 115 116 104 110 90Z"
                fill="rgba(255,255,255,0.14)"/>
          <path d="M110 88 C110 104 111 118 115 134"
                stroke="rgba(255,255,255,0.22)" stroke-width="6" stroke-linecap="round"/>
        </svg>
      </div>
    </div>

    <div class="center">
      <div class="dday">
        <div class="big">{dday_label}</div>
        <div class="sub">D-day Countdown</div>
        <div class="date">2026-11-19 · KST</div>
        <div class="deep">Deep Dive</div>
      </div>
    </div>

    <div class="hint">은하수 아래, 바다 생물들과 함께 · 아래 버튼으로 페이지 이동</div>

    <div class="nav">
      <a href="{PAGE_URL}">📘 지수·로그로 이동</a>
    </div>
  </div>
</body>
</html>
"""

# ✅ 이게 핵심: markdown이 아니라 components.html로 통째로 렌더
components.html(html, height=900, scrolling=False)

# 사이드바에도 링크(보험)
with st.sidebar:
    st.markdown("### 📄 Pages")
    st.page_link("pages/1.지수log.py", label="📘 지수·로그", use_container_width=True)
    st.page_link("pages/01.log.py", label="🚀 Deep dive: 지수·log")
