import streamlit as st

st.set_page_config(page_title="SM 수학사무소", layout="wide")

# 사이드바는 남겨두되, 메인은 애니메이션만
st.markdown(
    """
    <style>
    /* 전체 여백 제거 */
    [data-testid="stAppViewContainer"] { padding: 0rem; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    [data-testid="stToolbar"] { right: 1rem; }

    /* 메인 화면(대문) */
    .hero {
      position: relative;
      width: 100%;
      height: calc(100vh - 0px);
      overflow: hidden;
      border-radius: 0px;
      background: radial-gradient(1200px 600px at 20% 30%, rgba(99,102,241,0.30), transparent 60%),
                  radial-gradient(900px 500px at 80% 70%, rgba(16,185,129,0.22), transparent 60%),
                  linear-gradient(135deg, #050816 0%, #0b1220 45%, #050816 100%);
    }

    /* 움직이는 그라디언트 레이어 */
    .glow {
      position: absolute;
      inset: -40%;
      background: conic-gradient(from 180deg, rgba(99,102,241,0.10), rgba(251,191,36,0.10), rgba(16,185,129,0.10), rgba(99,102,241,0.10));
      filter: blur(60px);
      opacity: 0.75;
      animation: drift 10s linear infinite;
    }
    @keyframes drift {
      0%   { transform: translate3d(-6%, -4%, 0) rotate(0deg) scale(1.05); }
      50%  { transform: translate3d( 6%,  5%, 0) rotate(180deg) scale(1.10); }
      100% { transform: translate3d(-6%, -4%, 0) rotate(360deg) scale(1.05); }
    }

    /* 스캔 라인 */
    .scanline {
      position: absolute;
      left: 0; right: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent, rgba(251,191,36,0.7), transparent);
      opacity: 0.55;
      animation: scan 3.6s ease-in-out infinite;
    }
    @keyframes scan {
      0%   { top: -5%; }
      50%  { top: 55%; }
      100% { top: 105%; }
    }

    /* 파티클(점) 느낌: box-shadow로 여러 점 생성 */
    .stars {
      position: absolute;
      inset: 0;
      opacity: 0.55;
      background:
        radial-gradient(circle at 15% 25%, rgba(255,255,255,0.9) 0 1px, transparent 2px),
        radial-gradient(circle at 35% 65%, rgba(255,255,255,0.7) 0 1px, transparent 2px),
        radial-gradient(circle at 70% 30%, rgba(255,255,255,0.6) 0 1px, transparent 2px),
        radial-gradient(circle at 85% 80%, rgba(255,255,255,0.55) 0 1px, transparent 2px),
        radial-gradient(circle at 55% 45%, rgba(255,255,255,0.75) 0 1px, transparent 2px);
      animation: twinkle 2.8s ease-in-out infinite alternate;
    }
    @keyframes twinkle {
      from { opacity: 0.35; transform: scale(1.00); }
      to   { opacity: 0.70; transform: scale(1.02); }
    }

    /* 중앙 로고 */
    .center {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 32px;
      text-align: center;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 18px 22px;
      border-radius: 22px;
      border: 1px solid rgba(255,255,255,0.10);
      background: rgba(255,255,255,0.04);
      backdrop-filter: blur(10px);
      box-shadow: 0 20px 60px rgba(0,0,0,0.35);
      transform: translateY(0px);
      animation: floaty 2.6s ease-in-out infinite;
    }
    @keyframes floaty {
      0%   { transform: translateY(0px); }
      50%  { transform: translateY(-10px); }
      100% { transform: translateY(0px); }
    }

    .mark {
      width: 54px;
      height: 54px;
      border-radius: 18px;
      display: grid;
      place-items: center;
      font-weight: 900;
      letter-spacing: 0.5px;
      color: #0b1220;
      background: linear-gradient(135deg, rgba(251,191,36,1), rgba(99,102,241,1));
      box-shadow: 0 10px 30px rgba(99,102,241,0.25);
    }

    .title {
      font-size: 34px;
      font-weight: 900;
      line-height: 1.05;
      color: rgba(255,255,255,0.95);
      letter-spacing: -0.5px;
    }

    .subtitle {
      margin-top: 6px;
      font-size: 15px;
      font-weight: 700;
      color: rgba(199,210,254,0.85);
    }

    .hint {
      margin-top: 14px;
      font-size: 13px;
      font-weight: 700;
      color: rgba(255,255,255,0.55);
    }

    /* 작은 커서 깜빡임 */
    .cursor {
      display: inline-block;
      width: 10px;
      height: 18px;
      margin-left: 4px;
      background: rgba(251,191,36,0.9);
      animation: blink 1s steps(1) infinite;
      vertical-align: -3px;
      border-radius: 3px;
    }
    @keyframes blink { 50% { opacity: 0; } }
    </style>

    <div class="hero">
      <div class="glow"></div>
      <div class="stars"></div>
      <div class="scanline"></div>

      <div class="center">
        <div>
          <div class="badge">
            <div class="mark">SM</div>
            <div style="text-align:left;">
              <div class="title">수학사무소<span class="cursor"></span></div>
              <div class="subtitle">Investigation Mode · Approximation / Error / Tangent</div>
            </div>
          </div>
          <div class="hint">왼쪽 사이드바에서 활동 페이지로 이동</div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
