import streamlit as st
import random

# ✅ 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 0
if "industry" not in st.session_state:
    st.session_state.industry = ""
if "industry_confirmed" not in st.session_state:
    st.session_state.industry_confirmed = False
if "company_name" not in st.session_state:
    st.session_state.company_name = ""
if "situation" not in st.session_state:
    st.session_state.situation = ""
    st.session_state.options = []
if "selected_strategy" not in st.session_state:
    st.session_state.selected_strategy = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "crisis_situation" not in st.session_state:
    st.session_state.crisis_situation = ""
    st.session_state.crisis_options = []

# ✅ 스타일 정의 (말풍선 배경 rgba(255,255,255,0.1)로 복원)
st.markdown("""
<style>
/* 전체 앱 배경 및 기본 텍스트 */
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
}
h1, h2, h3, h4, h5, h6, label, p, span, div {
    color: #ffffff !important;
}

/* ✅ selectbox 영역: 배경 흰색, 텍스트는 검정색 */
div[data-baseweb="select"] {
    background-color: #ffffff !important;
}
div[data-baseweb="select"] * {
    color: #000000 !important;
    fill: #000000 !important;
}
.css-1dimb5e-singleValue,
.css-1jqq78o-placeholder,
.css-11unzgr,
.css-1n76uvr,
.css-qc6sy-singleValue,
.css-1wa3eu0-placeholder,
.css-1uccc91-singleValue,
div[role="listbox"] div {
    color: #000000 !important;
}

/* 버튼 텍스트 */
button p {
    color: #000000 !important;
    font-weight: bold;
}

/* 말풍선 UI 구성 – 기존 그대로 유지 */
.container {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    margin: 0;
    padding: 0;
    background-color: #1a1a1a;
}
.bg-image {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100vh;
    object-fit: cover;
    z-index: 0;
}
.speech-bubble {
    position: absolute;
    bottom: 8vh;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 500px;
    background: rgba(255, 255, 255, 0.1);
    padding: 20px 25px;
    border-radius: 25px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    text-align: center;
    z-index: 1;
    backdrop-filter: blur(8px);
}
.speech-title {
    font-size: 1.4rem;
    font-weight: bold;
    color: #ffffff;
}
.speech-sub {
    margin-top: 10px;
    font-size: 1rem;
    color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# ✅ 말풍선 출력 함수
def show_speech(title: str, subtitle: str, image_url: str):
    st.markdown(f"""
    <div class="container">
        <img src="{image_url}" class="bg-image">
        <div class="speech-bubble">
            <div class="speech-title">{title}</div>
            <div class="speech-sub">{subtitle}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ✅ Step 5: 국가적 위기 대응
if st.session_state.step == 5:
    show_speech("“국가적 위기 발생!”", "경제, 정치, 국제 환경이 급변하고 있어. 대응 전략이 필요해.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")

    crisis_situations = {
        "📉 한국 외환시장 급변 (원화 가치 급락)": ["환 헤지 강화", "수출 확대", "정부와 협력", "외환 보유 확대", "위기 커뮤니케이션"],
        "🇺🇸 미 연준의 기준금리 급등": ["대출 축소", "내수 집중 전략", "고금리 대비 자산 조정", "비용 구조 개선", "긴축 경영"],
        "🗳️ 윤석열 대통령 탄핵 가결": ["리스크 분산 경영", "정치 모니터링 강화", "내부 의사결정 체계 정비", "단기 전략 전환", "위기 대비 태스크포스 운영"],
        "🇺🇸 트럼프 대선 재당선": ["미국 중심 전략 강화", "공급망 재편", "관세 대비 물류 최적화", "현지 생산 강화", "미국 투자 확대"],
        "🛃 주요 국가의 관세 인상 정책": ["무역 파트너 다변화", "현지 생산 확대", "비관세 수출 전략", "신시장 개척", "가격 재설정"]
    }

    if not st.session_state.crisis_situation:
        st.session_state.crisis_situation, st.session_state.crisis_options = random.choice(list(crisis_situations.items()))

    st.markdown("### Step 5: 국가적 위기 대응")
    st.markdown(f"**상황:** {st.session_state.crisis_situation}")
    selected = st.radio("당신의 대응 전략은?", st.session_state.crisis_options)

    best_strategies = {
        "📉 한국 외환시장 급변 (원화 가치 급락)": "환 헤지 강화",
        "🇺🇸 미 연준의 기준금리 급등": "고금리 대비 자산 조정",
        "🗳️ 윤석열 대통령 탄핵 가결": "리스크 분산 경영",
        "🇺🇸 트럼프 대선 재당선": "공급망 재편",
        "🛃 주요 국가의 관세 인상 정책": "무역 파트너 다변화"
    }

    if st.button("전략 확정"):
        st.session_state.selected_strategy = selected
        if selected == best_strategies.get(st.session_state.crisis_situation):
            st.session_state.score += 10
        else:
            st.session_state.score += 5
        st.session_state.step = 6
        st.rerun()
