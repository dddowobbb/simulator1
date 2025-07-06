import streamlit as st
import random

# ✅ 세션 상태 초기화
def initialize_state():
    defaults = {
        "step": 0,
        "industry": "",
        "industry_confirmed": False,
        "company_name": "",
        "situation": "",
        "options": [],
        "selected_strategy": "",
        "score": 0,
        "crisis_situation": "",
        "crisis_options": []
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

initialize_state()

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
    <div class="container">
        <img src="{image_url}" class="bg-image">
        <div class="speech-bubble">
            <div class="speech-title">{title}</div>
            <div class="speech-sub">{subtitle}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ✅ Step 0: 시작
if st.session_state.step == 0:
    show_speech("“환영합니다!”", "경영 시뮬레이션에 오신 것을 환영합니다.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    if st.button("게임 시작 ▶️"):
        st.session_state.step = 1
        st.rerun()

# ✅ Step 1: 업종 선택
elif st.session_state.step == 1:
    if not st.session_state.industry_confirmed:
        show_speech("“어떤 산업에 도전할까?”", "원하는 업종을 선택해보자.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
        industries = ["💻 IT 스타트업", "🌱 친환경 제품", "🎮 게임 개발사", "👗 패션 브랜드", "🍔 푸드테크", "🛒 글로벌 전자상거래"]
        selected = st.selectbox("회사 업종을 선택하세요", industries)
        if st.button("업종 확정"):
            st.session_state.industry = selected
            st.session_state.industry_confirmed = True
            st.session_state.step = 2
            st.rerun()

# ✅ Step 2: 회사 이름
elif st.session_state.step == 2:
    show_speech("“회사 이름을 지어보자.”", "멋진 이름을 기대하고 있겠어.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    name = st.text_input("회사 이름 입력:", max_chars=20)
    if st.button("이름 확정"):
        if name.strip():
            st.session_state.company_name = name.strip()
            st.session_state.step = 3
            st.rerun()

# ✅ Step 3: 위기 상황 - 전략 선택
elif st.session_state.step == 3:
    show_speech("“예기치 못한 사건 발생!”", "전략을 선택해 회사를 지켜내자.", "https://raw.githubusercontent.com/dddowobbb/simulator1/main/badevent.png")
    situations = {
        "📈 수요 폭증": ["생산 확대", "기술 투자", "인력 확충", "외주 활용"],
        "💸 원자재 급등": ["공급처 변경", "대체 소재", "장기계약", "원가 절감"]
    }
    best_strategies = {
        "📈 수요 폭증": "생산 확대",
        "💸 원자재 급등": "공급처 변경"
    }
    if not st.session_state.situation:
        st.session_state.situation, st.session_state.options = random.choice(list(situations.items()))
    st.write(f"상황: {st.session_state.situation}")
    choice = st.radio("전략 선택:", st.session_state.options)
    if st.button("전략 확정"):
        st.session_state.selected_strategy = choice
        st.session_state.score += 10 if choice == best_strategies[st.session_state.situation] else 5
        st.session_state.step = 4
        st.rerun()

# ✅ Step 4: 전략 피드백
elif st.session_state.step == 4:
    result = st.session_state.selected_strategy
    score = st.session_state.score
    title = "“탁월한 선택이었어!”" if score >= 10 else "“괜찮은 선택이지만 더 나은 전략도 있었지.”"
    subtitle = f"{result} 전략으로 점수: {score}점"
    show_speech(title, subtitle, "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    if st.button("다음 ▶️"):
        st.session_state.step = 5
        st.session_state.situation = ""
        st.session_state.options = []
        st.session_state.selected_strategy = ""
        st.rerun()

# ✅ Step 5: 내부 문제
elif st.session_state.step == 5:
    issues = {"조직문화 혁신": 10, "복지 강화": 8, "리더 교체": 6, "교육 강화": 7, "방치": 2}
    if "step5_done" not in st.session_state:
        show_speech("“조직 내 문제가 발생했어!”", "직원 사기 저하와 갈등이 보고됐어.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
        sel = st.radio("해결 전략 선택:", list(issues.keys()))
        if st.button("전략 확정"):
            st.session_state.selected_strategy = sel
            st.session_state.score += issues[sel]
            st.session_state.step5_done = True
            st.rerun()
    else:
        result = st.session_state.selected_strategy
        show_speech("“잘 처리했군.”", f"{result} 전략으로 점수: {st.session_state.score}점", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
        if st.button("다음 ▶️"):
            del st.session_state.step5_done
            st.session_state.step = 6
            st.session_state.selected_strategy = ""
            st.rerun()

# ✅ Step 6: 외부 돌발 변수
elif st.session_state.step == 6:
    events = {
        "글로벌 경제 불황": {"options": ["내수 집중", "긴축 재정", "비용 절감"], "best": "내수 집중"},
        "경쟁사 신제품 출시": {"options": ["기술 투자", "마케팅 강화", "가격 인하"], "best": "기술 투자"}
    }
    if "step6_done" not in st.session_state:
        if "event_6" not in st.session_state:
            name, info = random.choice(list(events.items()))
            st.session_state.event_6 = name
            st.session_state.event_6_options = info["options"]
            st.session_state.event_6_best = info["best"]
        show_speech("“예상치 못한 변수 등장!”", st.session_state.event_6, "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
        selected = st.radio("전략 선택:", st.session_state.event_6_options)
        if st.button("전략 확정"):
            st.session_state.selected_strategy = selected
            st.session_state.score += 10 if selected == st.session_state.event_6_best else 5
            st.session_state.step6_done = True
            st.rerun()
    else:
        show_speech("“위기에도 잘 대처했군.”", f"전략: {st.session_state.selected_strategy}, 총점: {st.session_state.score}점", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
        if st.button("다음 ▶️"):
            for k in ["event_6", "event_6_options", "event_6_best", "step6_done"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.session_state.step = 7
            st.session_state.selected_strategy = ""
            st.rerun()
