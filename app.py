import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo

st.set_page_config(page_title="SM 수학사무소", layout="wide")

# ----------------------------
# D-day (Asia/Seoul)
# ----------------------------
KST = ZoneInfo("Asia/Seoul")
today = datetime.now(KST).date()
target = date(2026, 11, 19)
dday = (target - today).days

dday_label = f"D-{dday}" if dday > 0 else ("D-DAY" if dday == 0 else f"D+{abs(dday)}")

# ----------------------------
# Pages 링크
# - Streamlit 1.32+ 에서는 st.page_link 권장
# - 버튼이 안 뜨면 requirements.txt에서 streamlit 최신으로 올리면 됨
# ----------------------------
st.markdown(
    f"""
    <style>
    /* 전체 여백 최소화 */
    [data-testid="stAppViewContainer"] {{ padding: 0rem; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
    [data-testid="stToolbar"] {{ right: 1rem; }}

    .hero {{
      position: relative;
      width: 100%;
      height: 100vh;
      overflow: hidden;
      background:
        radial-gradient(1200px 700px at 20% 30%, rgba(99,102,241,0.28), transparent 60%),
        radial-gradient(900px 600px at 82% 72%, rgba(16,185,129,0.18), transparent 62%),
        linear-gradient(160deg, #040714 0%, #071226 45%, #02040b 100%);
    }}

    /* 우주(별) 레이어 */
    .stars {{
      position: absolute;
      inset: 0;
      opacity: 0.70;
      background:
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.95) 0 1px, transparent 2px),
        radial-gradient(circle at 22% 65%, rgba(255,255,255,0.75) 0 1px, transparent 2px),
        radial-gradient(circle at 44% 35%, rgba(255,255,255,0.60) 0 1px, transparent 2px),
        radial-gradient(circle at 63% 18%, rgba(255,255,255,0.70) 0 1px, transparent 2px),
        radial-gradient(circle at 78% 52%, rgba(255,255,255,0.55) 0 1px, transparent 2px),
        radial-gradient(circle at 90% 28%, rgba(255,255,255,0.65) 0 1px, transparent 2px);
      animation: twinkle 2.9s ease-in-out infinite alternate;
    }}
    @keyframes twinkle {{
      from {{ opacity: 0.35; transform: scale(1.00); }}
      to   {{ opacity: 0.75; transform: scale(1.02); }}
    }}

    /* 오로라/우주 먼지 */
    .nebula {{
      position: absolute;
      inset: -40%;
      background: conic-gradient(
        from 200deg,
        rgba(99,102,241,0.10),
        rgba(251,191,36,0.08),
        rgba(16,185,129,0.08),
        rgba(99,102,241,0.10)
      );
      filter: blur(70px);
      opacity: 0.70;
      animation: drift 11s linear infinite;
    }}
    @keyframes drift {{
      0%   {{ transform: translate3d(-6%, -4%, 0) rotate(0deg) scale(1.05); }}
      50%  {{ transform: translate3d( 6%,  5%, 0) rotate(180deg) scale(1.10); }}
      100% {{ transform: translate3d(-6%, -4%, 0) rotate(360deg) scale(1.05); }}
    }}

    /* 바다(파도) 레이어: 아래쪽 그라디언트 + 움직이는 물결 */
    .ocean {{
      position: absolute;
      left: 0; right: 0; bottom: 0;
      height: 42vh;
      background:
        radial-gradient(900px 220px at 30% 40%, rgba(59,130,246,0.22), transparent 65%),
        radial-gradient(700px 200px at 80% 70%, rgba(16,185,129,0.14), transparent 65%),
        linear-gradient(180deg, rgba(2,6,23,0) 0%, rgba(2,6,23,0.35) 18%, rgba(2,6,23,0.88) 100%);
    }}
    .wave {{
      position: absolute;
      left: -25%;
      width: 150%;
      height: 70px;
      bottom: 14vh;
      background: rgba(255,255,255,0.04);
      border-radius: 999px;
      filter: blur(0.5px);
      animation: wave 7s ease-in-out infinite;
    }}
    .wave.wave2 {{
      bottom: 10vh;
      height: 54px;
      opacity: 0.7;
      animation-duration: 9s;
      animation-direction: reverse;
    }}
    .wave.wave3 {{
      bottom: 6vh;
      height: 46px;
      opacity: 0.5;
      animation-duration: 11s;
    }}
    @keyframes wave {{
      0%   {{ transform: translateX(0%)   scaleY(1); }}
      50%  {{ transform: translateX(6%)   scaleY(1.15); }}
      100% {{ transform: translateX(0%)   scaleY(1); }}
    }}

    /* 중앙 패널(투명 카드) */
    .center {{
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 32px;
      text-align: center;
    }}

    .panel {{
      width: min(860px, 92vw);
      padding: 20px 22px;
      border-radius: 26px;
      border: 1px solid rgba(255,255,255,0.12);
      background: rgba(255,255,255,0.05);
      backdrop-filter: blur(12px);
      box-shadow: 0 24px 70px rgba(0,0,0,0.40);
      animation: floaty 2.8s ease-in-out infinite;
    }}
    @keyframes floaty {{
      0%   {{ transform: translateY(0px); }}
      50%  {{ transform: translateY(-10px); }}
      100% {{ transform: translateY(0px); }}
    }}

    .row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-align: left;
    }}

    .mark {{
      width: 52px; height: 52px;
      border-radius: 18px;
      display: grid;
      place-items: center;
      font-weight: 900;
      color: #071226;
      background: linear-gradient(135deg, rgba(251,191,36,1), rgba(99,102,241,1));
      box-shadow: 0 12px 30px rgba(99,102,241,0.22);
    }}

    .title {{
      font-size: 30px;
      font-weight: 900;
      letter-spacing: -0.6px;
      color: rgba(255,255,255,0.95);
      line-height: 1.05;
    }}
    .subtitle {{
      margin-top: 6px;
      font-size: 14px;
      font-weight: 800;
      color: rgba(199,210,254,0.85);
    }}

    .dday {{
      padding: 10px 14px;
      border-radius: 18px;
      border: 1px solid rgba(255,255,255,0.12);
      background: rgba(2,6,23,0.45);
      color: rgba(255,255,255,0.92);
      font-weight: 900;
      letter-spacing: 0.4px;
      text-align: right;
      min-width: 180px;
    }}
    .dday small {{
      display:block;
      margin-top:4px;
      font-weight: 800;
      color: rgba(165,180,252,0.85);
      letter-spacing: 0px;
    }}

    .hint {{
      margin-top: 10px;
      font-size: 13px;
      font-weight: 800;
      color: rgba(255,255,255,0.60);
    }}

    /* 아래 “pages로 이동” 영역은 Streamlit 컴포넌트로 따로 배치할 거라
       패널 안에는 안내만 둔다. */
    </style>

    <div class="hero">
      <div class="nebula"></div>
      <div class="stars"></div>

      <div class="ocean">
        <div class="wave"></div>
        <div class="wave wave2"></div>
        <div class="wave wave3"></div>
      </div>

      <div class="center">
        <div class="panel">
          <div class="row">
            <div class="brand">
              <div class="mark">SM</div>
              <div>
                <div class="title">수학사무소 · Deep Dive</div>
                <div class="subtitle">Space × Sea · Approximation / Error / Tangent</div>
              </div>
            </div>
            <div class="dday">
              {dday_label}
              <small>2026-11-19 (KST)</small>
            </div>
          </div>

          <div class="hint">
            아래 버튼으로 활동 페이지로 이동하세요. (왼쪽 사이드바에도 동일하게 표시됩니다)
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# “대문은 애니메이션만”을 최대한 유지하려면:
# 아래 버튼 영역도 최소 높이로, 배경 투명하게.
# ----------------------------
st.markdown(
    """
    <style>
    .stButton > button, .stLinkButton > a {
      border-radius: 18px !important;
      font-weight: 900 !important;
    }
    [data-testid="stVerticalBlock"] > div:has(> div[data-testid="stHorizontalBlock"]) {
      margin-top: -180px;   /* 패널 바로 아래에 붙게 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Pages 이동 버튼(가능하면 page_link 사용)
c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    try:
        st.page_link("pages/1.지수log.py", label="📘 지수·로그", use_container_width=True)
    except Exception:
        st.link_button("📘 지수·로그 (사이드바에서 이동)", "#", use_container_width=True)

with c2:
    # 네가 pages에 추가할 예정이라면 파일명만 맞추면 됨
    try:
        st.page_link("pages/2.root근사.py", label="🧩 Root 근사", use_container_width=True)
    except Exception:
        st.link_button("🧩 Root 근사 (pages/2.root근사.py 필요)", "#", use_container_width=True)

with c3:
    try:
        st.page_link("pages/3.limit.py", label="📉 Limit / 접선", use_container_width=True)
    except Exception:
        st.link_button("📉 Limit (pages/3.limit.py 필요)", "#", use_container_width=True)
