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

# ✅ 스타일 정의
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
}
h1, h2, h3, h4, h5, h6, label, p, span, div {
    color: #ffffff !important;
}
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
button p {
    color: #000000 !important;
    font-weight: bold;
}
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
    <div class=\"container\">
        <img src=\"{image_url}\" class=\"bg-image\">
        <div class=\"speech-bubble\">
            <div class=\"speech-title\">{title}</div>
            <div class=\"speech-sub\">{subtitle}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ✅ Step 0: 시작 안내
if st.session_state.step == 0:
    show_speech("“환영합니다!”", "게임 플레이에 앞서 다크모드를 적용중이시라면 라이트모드로 전환해주시길 바랍니다.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    st.markdown("### 경영 시뮬레이션 게임에 오신 것을 환영합니다!")
    st.markdown("이 게임에서는 회사를 창업하고 성장시키는 과정에서 다양한 결정을 내려야 합니다. 회사를 성공적으로 운영해보세요!")
    if st.button("게임 시작 ▶️"):
        st.session_state.step = 1
        st.experimental_rerun()

# ✅ Step 1~6 처리: (기존 코드 유지)
# ... Step 1~6 코드는 기존대로 유지하며, 각 스텝 내부에서만 버튼 포함되도록 정리합니다.

# ✅ Step 6: 최종 평가
elif st.session_state.step == 6:
    if st.session_state.selected_strategy:
        if st.session_state.score >= 20:
            title = "“최고의 경영자군!”"
            subtitle = f"{st.session_state.selected_strategy} 전략은 위기 속에서도 뛰어난 선택이었어. 총 점수: {st.session_state.score}점"
        else:
            title = "“괜찮은 성과지만 아직 성장 가능성이 보여.”"
            subtitle = f"{st.session_state.selected_strategy} 전략은 나쁘지 않았어. 총 점수: {st.session_state.score}점"
    else:
        title = "“전략 없이 위기를 넘기긴 어렵지.”"
        subtitle = "전략을 선택하지 않았어. 다음번엔 더 나은 결정을 기대할게."

    show_speech(title, subtitle, "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")

    st.markdown("### Step 6: 최종 결과")
    st.success(f"당신의 최종 전략: **{st.session_state.selected_strategy}**")
    st.info(f"최종 점수: **{st.session_state.score}점**")

    if st.button("다음 ▶️"):
        st.session_state.step = 7
        st.experimental_rerun()


# ✅ Step 7: 내부 문제 해결
elif st.session_state.step == 7:
    show_speech("“요즘 직원들 분위기가 심상치 않아...”", "사기 저하, 인사 갈등, 생산성 저하 문제가 보고됐어. 어떻게 대응할까?", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")

    st.markdown("### Step 7: 내부 문제 해결 전략 선택")

    org_issues = {
        "🧠 조직문화 혁신": 10,
        "💰 복지 강화": 8,
        "🔁 리더십 교체": 6,
        "📚 교육 강화": 7,
        "🧘 그냥 기다린다": 2
    }

    selected_org_strategy = st.radio("내부 문제를 해결할 전략을 선택하세요:", list(org_issues.keys()))

    if st.button("전략 확정"):
        st.session_state.selected_strategy = selected_org_strategy
        st.session_state.score += org_issues[selected_org_strategy]
        st.session_state.step = 8
        st.rerun()
# ✅ Step 8: 돌발 변수 등장
elif st.session_state.step == 8:
    show_speech("“뜻밖의 일이 벌어졌어!”", "외부 변수로 인해 경영환경이 크게 흔들리고 있어.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")

    st.markdown("### Step 8: 돌발 변수 등장")

    random_events = {
        "📉 글로벌 경제 불황": {
            "options": ["비용 절감", "내수 시장 집중", "긴축 재정 운영", "신사업 보류", "시장 철수"],
            "best": "내수 시장 집중"
        },
        "🚀 경쟁사의 혁신 제품 발표": {
            "options": ["기술 개발 가속", "브랜드 리뉴얼", "마케팅 강화", "가격 인하", "특허 소송"],
            "best": "기술 개발 가속"
        },
        "📜 정부 규제 강화": {
            "options": ["법무팀 확대", "규제 준수 시스템 강화", "비즈니스 모델 전환", "로비 활동 강화", "해외 진출 모색"],
            "best": "규제 준수 시스템 강화"
        }
    }

    if "event_8" not in st.session_state:
        event_name, event_info = random.choice(list(random_events.items()))
        st.session_state.event_8 = event_name
        st.session_state.event_8_options = event_info["options"]
        st.session_state.event_8_best = event_info["best"]

    st.markdown(f"**🌀 이벤트:** {st.session_state.event_8}")
    selected_event_strategy = st.radio("✅ 어떤 전략으로 대응할까요?", st.session_state.event_8_options)

    if st.button("전략 확정"):
        st.session_state.selected_strategy = selected_event_strategy
        if selected_event_strategy == st.session_state.event_8_best:
            st.session_state.score += 10
        else:
            st.session_state.score += 5
        del st.session_state["event_8"]
        del st.session_state["event_8_options"]
        del st.session_state["event_8_best"]
        st.session_state.step = 9
        st.rerun()



