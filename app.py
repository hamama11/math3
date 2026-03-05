import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo

st.set_page_config(page_title="SM 수학사무소", layout="wide")

# ---- D-day (KST) ----
KST = ZoneInfo("Asia/Seoul")
today = datetime.now(KST).date()
target = date(2026, 11, 19)
dday = (target - today).days
dday_label = f"D-{dday}" if dday > 0 else ("D-DAY" if dday == 0 else f"D+{abs(dday)}")

# ---- 현재 pages는 1개(지수log)만 ----
PAGE_PATH = "pages/1.지수log.py"

# ---- 메인: 애니메이션 대문(HTML/CSS) ----
st.markdown(
    f"""
    <style>
    /* Streamlit 기본 여백 최소화 */
    [data-testid="stAppViewContainer"] {{ padding: 0rem; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
    [data-testid="stToolbar"] {{ right: 1rem; }}

    /* 메인 영역 높이 확보 */
    .block-container {{ padding-top: 0rem; padding-bottom: 0rem; }}

    .hero {{
      position: relative;
      width: 100%;
      height: 100vh;
      overflow: hidden;

      /* 🔆 조금 더 밝게 */
      background:
        radial-gradient(1200px 700px at 25% 30%, rgba(99,102,241,0.30), transparent 60%),
        radial-gradient(900px 600px at 82% 72%, rgba(16,185,129,0.18), transparent 62%),
        linear-gradient(160deg, #07102a 0%, #0b1a36 48%, #050a18 100%);
    }}

    /* 은하수 밴드(좀 더 선명) */
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

    /* 별(촘촘하게) */
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

    /* 바다(조금 더 밝게) */
    .ocean {{
      position:absolute; left:0; right:0; bottom:0;
      height: 46vh;
      background:
        radial-gradient(1000px 260px at 28% 40%, rgba(59,130,246,0.26), transparent 65%),
        radial-gradient(800px 240px at 82% 70%, rgba(16,185,129,0.16), transparent 65%),
        linear-gradient(180deg, rgba(2,6,23,0) 0%, rgba(2,6,23,0.30) 18%, rgba(2,6,23,0.90) 100%);
    }}

    /* 파도 레이어 */
    .wave {{
      position:absolute;
      left:-25%; width:150%;
      height: 70px;
      bottom: 14vh;
      background: rgba(255,255,255,0.055);
      border-radius: 999px;
      animation: wave 7s ease-in-out infinite;
      filter: blur(0.3px);
    }}
    .wave.w2 {{ bottom: 10vh; height: 56px; opacity: 0.70; animation-duration: 9s; animation-direction: reverse; }}
    .wave.w3 {{ bottom:  6vh; height: 48px; opacity: 0.55; animation-duration: 11s; }}
    @keyframes wave {{
      0%   {{ transform: translateX(0%)   scaleY(1); }}
      50%  {{ transform: translateX(6%)   scaleY(1.18); }}
      100% {{ transform: translateX(0%)   scaleY(1); }}
    }}

    /* 중앙 D-day 크게 + Deep Dive */
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
      color: rgba(255,255,255,0.96);
      text-shadow: 0 18px 60px rgba(0,0,0,0.55);
      line-height: 1.0;
      user-select: none;
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

    /* 유영 생물(이모지 + SVG 만타) */
    .swim {{
      position:absolute;
      left: -22%;
      bottom: 16vh;
      font-size: 46px;
      filter: drop-shadow(0 10px 30px rgba(0,0,0,0.45));
      opacity: 0.95;
      user-select: none;
      will-change: transform;
      animation: swim 18s linear infinite, bob 2.6s ease-in-out infinite;
    }}
    .swim.whale1 {{
      bottom: 19vh; font-size: 58px;
      animation-duration: 24s;
      opacity: 0.92;
    }}
    .swim.turtle {{
      bottom: 12vh; font-size: 46px;
      animation-duration: 20s;
      opacity: 0.92;
    }}
    .swim.whale2 {{
      bottom: 8vh; font-size: 50px;
      animation-duration: 28s;
      opacity: 0.78;
      filter: drop-shadow(0 10px 30px rgba(0,0,0,0.55)) blur(0.2px);
    }}

    /* 만타 SVG는 크기 따로 */
    .manta {{
      bottom: 14vh;
      width: 92px;
      height: 62px;
      opacity: 0.88;
      animation-duration: 23s;
      filter: drop-shadow(0 12px 28px rgba(0,0,0,0.55));
    }}
    .manta svg {{
      width: 100%;
      height: 100%;
    }}

    @keyframes swim {{
      0%   {{ transform: translateX(0vw); }}
      100% {{ transform: translateX(145vw); }}
    }}
    @keyframes bob {{
      0%,100% {{ transform: translateY(0px); }}
      50%     {{ transform: translateY(-10px); }}
    }}

    /* 하단 안내 */
    .hint {{
      position:absolute;
      left: 50%;
      transform: translateX(-50%);
      bottom: 70px; /* 플로팅 바 위로 올림 */
      font-size: 13px;
      font-weight: 850;
      color: rgba(255,255,255,0.62);
      user-select: none;
      text-align: center;
      padding: 8px 12px;
      border-radius: 999px;
      background: rgba(2,6,23,0.32);
      border: 1px solid rgba(255,255,255,0.10);
      backdrop-filter: blur(10px);
    }}

    /* 플로팅 버튼 바(페이지 이동용) */
    .floating {{
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
      pointer-events: none; /* 아래 st.page_link 클릭 방해 방지 */
    }}

    /* Streamlit의 page_link 버튼을 플로팅바 위치로 끌어올리는 컨테이너 */
    .dock {{
      position: fixed;
      left: 50%;
      transform: translateX(-50%);
      bottom: 18px;
      z-index: 10000;
      width: min(520px, 92vw);
      pointer-events: auto;
    }}
    </style>

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

        <!-- 만타 가오리: SVG 실루엣 -->
        <div class="swim manta" aria-label="manta">
          <svg viewBox="0 0 220 140" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M110 20
                     C75 22 40 45 22 78
                     C10 100 22 122 48 114
                     C70 108 88 90 110 90
                     C132 90 150 108 172 114
                     C198 122 210 100 198 78
                     C180 45 145 22 110 20Z"
                  fill="rgba(255,255,255,0.18)"/>
            <path d="M110 90 C104 104 98 115 86 126
                     C102 120 108 112 110 104
                     C112 112 118 120 134 126
                     C122 115 116 104 110 90Z"
                  fill="rgba(255,255,255,0.14)"/>
            <path d="M110 88 C110 104 111 118 115 134" stroke="rgba(255,255,255,0.20)" stroke-width="6" stroke-linecap="round"/>
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
    </div>

    <!-- 플로팅 바(시각적 배경) -->
    <div class="floating"></div>
    """,
    unsafe_allow_html=True
)

# ---- 플로팅 버튼(현재 지수log 1개만) ----
# st.page_link는 Streamlit 버전에 따라 없을 수 있어서 try/except
st.markdown('<div class="dock">', unsafe_allow_html=True)
c1, c2 = st.columns([1, 1], vertical_alignment="center")
with c1:
    try:
        st.page_link(PAGE_PATH, label="📘 지수·로그로 이동", use_container_width=True)
    except Exception:
        st.link_button("📘 지수·로그(사이드바)", "#", use_container_width=True)
with c2:
    st.link_button("🧭 사이드바 열기", "#", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---- 사이드바에도 유지 ----
with st.sidebar:
    st.markdown("### 📄 Pages")
    try:
        st.page_link(PAGE_PATH, label="📘 지수·로그", use_container_width=True)
    except Exception:
        st.write("왼쪽 Pages에서 지수·로그 선택")
