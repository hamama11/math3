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

st.markdown(
    f"""
    <style>
    /* Streamlit 기본 여백 최소화 */
    [data-testid="stAppViewContainer"] {{ padding: 0rem; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
    [data-testid="stToolbar"] {{ right: 1rem; }}

    .hero {{
      position: relative;
      width: 100%;
      height: 100vh;
      overflow: hidden;
      background:
        radial-gradient(1200px 700px at 25% 30%, rgba(99,102,241,0.22), transparent 60%),
        radial-gradient(900px 600px at 82% 72%, rgba(16,185,129,0.12), transparent 62%),
        linear-gradient(160deg, #040714 0%, #071226 48%, #02040b 100%);
    }}

    /* 은하수 밴드(움직이는 빛) */
    .milkyway {{
      position:absolute; inset:-40%;
      background:
        radial-gradient(closest-side at 50% 50%, rgba(255,255,255,0.10), transparent 62%),
        conic-gradient(from 240deg,
          rgba(255,255,255,0.06),
          rgba(99,102,241,0.10),
          rgba(251,191,36,0.06),
          rgba(16,185,129,0.08),
          rgba(255,255,255,0.06)
        );
      filter: blur(70px);
      opacity: 0.75;
      animation: drift 12s linear infinite;
      mix-blend-mode: screen;
    }}
    @keyframes drift {{
      0%   {{ transform: translate3d(-6%, -4%, 0) rotate(0deg) scale(1.05); }}
      50%  {{ transform: translate3d( 6%,  5%, 0) rotate(180deg) scale(1.10); }}
      100% {{ transform: translate3d(-6%, -4%, 0) rotate(360deg) scale(1.05); }}
    }}

    /* 별(반짝임) */
    .stars {{
      position:absolute; inset:0;
      opacity: 0.75;
      background:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.95) 0 1px, transparent 2px),
        radial-gradient(circle at 18% 62%, rgba(255,255,255,0.70) 0 1px, transparent 2px),
        radial-gradient(circle at 35% 32%, rgba(255,255,255,0.55) 0 1px, transparent 2px),
        radial-gradient(circle at 52% 18%, rgba(255,255,255,0.65) 0 1px, transparent 2px),
        radial-gradient(circle at 66% 48%, rgba(255,255,255,0.50) 0 1px, transparent 2px),
        radial-gradient(circle at 78% 28%, rgba(255,255,255,0.60) 0 1px, transparent 2px),
        radial-gradient(circle at 90% 70%, rgba(255,255,255,0.45) 0 1px, transparent 2px);
      animation: twinkle 3s ease-in-out infinite alternate;
    }}
    @keyframes twinkle {{
      from {{ opacity: 0.35; }}
      to   {{ opacity: 0.85; }}
    }}

    /* 바다(하단 그라디언트) */
    .ocean {{
      position:absolute; left:0; right:0; bottom:0;
      height: 46vh;
      background:
        radial-gradient(900px 240px at 28% 40%, rgba(59,130,246,0.18), transparent 65%),
        radial-gradient(700px 220px at 82% 70%, rgba(16,185,129,0.10), transparent 65%),
        linear-gradient(180deg, rgba(2,6,23,0) 0%, rgba(2,6,23,0.35) 18%, rgba(2,6,23,0.92) 100%);
    }}

    /* 파도 레이어 */
    .wave {{
      position:absolute;
      left:-25%; width:150%;
      height: 68px;
      bottom: 14vh;
      background: rgba(255,255,255,0.04);
      border-radius: 999px;
      animation: wave 7s ease-in-out infinite;
      filter: blur(0.5px);
    }}
    .wave.w2 {{ bottom: 10vh; height: 54px; opacity: 0.65; animation-duration: 9s; animation-direction: reverse; }}
    .wave.w3 {{ bottom:  6vh; height: 46px; opacity: 0.50; animation-duration: 11s; }}
    @keyframes wave {{
      0%   {{ transform: translateX(0%)   scaleY(1); }}
      50%  {{ transform: translateX(6%)   scaleY(1.18); }}
      100% {{ transform: translateX(0%)   scaleY(1); }}
    }}

    /* D-day: 정중앙 크게 */
    .center {{
      position:absolute; inset:0;
      display:flex; align-items:center; justify-content:center;
      text-align:center;
      padding: 24px;
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
      font-size: min(14vw, 128px);
      background: linear-gradient(135deg, rgba(251,191,36,1), rgba(99,102,241,1), rgba(16,185,129,1));
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      filter: drop-shadow(0 16px 32px rgba(99,102,241,0.25));
    }}
    .dday .sub {{
      margin-top: 10px;
      font-size: min(3.8vw, 26px);
      font-weight: 900;
      color: rgba(199,210,254,0.90);
    }}
    .dday .date {{
      margin-top: 6px;
      font-size: min(3.2vw, 18px);
      font-weight: 800;
      color: rgba(255,255,255,0.60);
    }}

    /* 유영하는 생물(이모지) */
    .swim {{
      position:absolute;
      left: -18%;
      bottom: 16vh;
      font-size: 44px;
      filter: drop-shadow(0 10px 30px rgba(0,0,0,0.45));
      opacity: 0.92;
      user-select: none;
      will-change: transform;
      animation: swim 18s linear infinite, bob 2.6s ease-in-out infinite;
    }}
    .swim.whale1 {{
      bottom: 18vh; font-size: 54px;
      animation-duration: 22s;
      opacity: 0.90;
    }}
    .swim.whale2 {{
      bottom: 9vh; font-size: 46px;
      animation-duration: 26s;
      opacity: 0.78;
      filter: drop-shadow(0 10px 30px rgba(0,0,0,0.55)) blur(0.2px);
    }}
    @keyframes swim {{
      0%   {{ transform: translateX(0vw); }}
      100% {{ transform: translateX(140vw); }}
    }}
    @keyframes bob {{
      0%,100% {{ transform: translateY(0px); }}
      50%     {{ transform: translateY(-10px); }}
    }}

    /* 하단 작은 안내 (최소) */
    .hint {{
      position:absolute;
      left: 50%;
      transform: translateX(-50%);
      bottom: 22px;
      font-size: 13px;
      font-weight: 800;
      color: rgba(255,255,255,0.55);
      user-select: none;
      text-align: center;
      padding: 8px 12px;
      border-radius: 999px;
      background: rgba(2,6,23,0.35);
      border: 1px solid rgba(255,255,255,0.10);
      backdrop-filter: blur(10px);
    }}
    </style>

    <div class="hero">
      <div class="milkyway"></div>
      <div class="stars"></div>

      <div class="ocean">
        <div class="wave"></div>
        <div class="wave w2"></div>
        <div class="wave w3"></div>

        <!-- 바다 생물 -->
        <div class="swim">🐢</div>
        <div class="swim whale1">🐋</div>
        <div class="swim whale2">🐋</div>
      </div>

      <div class="center">
        <div class="dday">
          <div class="big">{dday_label}</div>
          <div class="sub">D-day Countdown</div>
          <div class="date">2026-11-19 · KST</div>
        </div>
      </div>

      <div class="hint">왼쪽 사이드바에서 ‘지수·로그’ 페이지로 이동</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- pages 이동: 지금은 지수log 하나만 ----
# 화면을 "애니메이션만"에 가깝게 유지하려면, 버튼을 굳이 본문에 추가하지 않고
# 사이드바만 쓰는 게 가장 깔끔함.
# 그래도 원하면 아래 한 줄만 켜면 "대문 아래에 버튼 1개"를 만들 수 있음.

with st.sidebar:
    st.markdown("### 📄 Pages")
    try:
        st.page_link("pages/1.지수log.py", label="📘 지수·로그", use_container_width=True)
    except Exception:
        st.write("사이드바에서 pages를 선택하세요.")
