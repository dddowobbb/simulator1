import streamlit as st
import random

# ✅ 세션 상태 초기화
default_states = {
    "step": 0, "industry": "", "industry_confirmed": False,
    "company_name": "", "situation": "", "options": [],
    "selected_strategy": "", "score": 0,
    "crisis_situation": "", "crisis_options": [],
    "event_8": "", "event_8_options": [], "event_8_best": ""
}
for key, val in default_states.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ✅ 스타일 적용 함수
def apply_custom_style():
    st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
    }
    h1, h2, h3, h4, h5, h6, label, p, span, div {
        color: #ffffff !important;
    }
    div[data-baseweb="select"], div[role="listbox"] div {
        background-color: #ffffff !important;
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

# ✅ 말풍선 함수
def show_speech(title, subtitle, img_url):
    st.markdown(f"""
    <div class="container">
        <img src="{img_url}" class="bg-image">
        <div class="speech-bubble">
            <div class="speech-title">{title}</div>
            <div class="speech-sub">{subtitle}</div>
        </div>
    </div>""", unsafe_allow_html=True)

# ✅ Step 함수 정의
def step_0():
    show_speech("“환영합니다!”", "다크모드 사용 중이면 라이트모드로 전환해주세요.", img)
    if st.button("게임 시작 ▶️"):
        st.session_state.step = 1
        st.rerun()

def step_1():
    industries = ["💻 IT 스타트업", "🌱 친환경 제품", "🎮 게임 개발사", "👗 패션 브랜드", "🍔 푸드테크", "🛒 글로벌 전자상거래"]
    if not st.session_state.industry_confirmed:
        show_speech("“이제 어떤 산업에 뛰어들지 정하자.”", "원하는 분야를 선택해줘.", img)
        selected = st.selectbox("업종 선택", industries)
        if st.button("업종 확정"):
            st.session_state.industry = selected
            st.session_state.industry_confirmed = True
            st.session_state.step = 2
            st.rerun()
    else:
        show_speech(f"“{st.session_state.industry}, 멋진 선택이야.”", "다음 단계로 넘어가자!", img)
        if st.button("다음 ▶️"):
            st.session_state.step = 2
            st.rerun()

def step_2():
    show_speech("“이제 회사를 만들 시간이야.”", "멋진 이름을 지어봐.", img)
    name = st.text_input("회사 이름", max_chars=20)
    if st.button("이름 확정") and name.strip():
        st.session_state.company_name = name.strip()
        st.rerun()
    if st.session_state.company_name:
        st.success(f"✅ 회사 이름: {st.session_state.company_name}")
        if st.button("다음 ▶️"):
            st.session_state.step = 3
            st.rerun()

def step_3():
    situations = {
        "⚠️ 데이터 유출": ["보안 재구축", "사과문", "PR 대응"],
        "📈 수요 폭증": ["라인 확장", "임시 고용", "외주 활용"]
    }
    best = {"⚠️ 데이터 유출": "보안 재구축", "📈 수요 폭증": "라인 확장"}
    if not st.session_state.situation:
        st.session_state.situation, st.session_state.options = random.choice(list(situations.items()))
    show_speech("“예기치 못한 사건 발생!”", st.session_state.situation, event_img)
    selected = st.radio("전략 선택", st.session_state.options)
    if st.button("전략 확정"):
        st.session_state.selected_strategy = selected
        st.session_state.score += 10 if selected == best[st.session_state.situation] else 5
        st.session_state.step = 4
        st.rerun()

def step_4():
    strat = st.session_state.selected_strategy
    score = st.session_state.score
    if score >= 10:
        show_speech("“훌륭한 전략이었어!”", f"{strat} 선택은 탁월했어! 점수: {score}", img)
    else:
        show_speech("“음... 더 나은 선택이 있었을지도.”", f"선택: {strat}, 점수: {score}", img)
    if st.button("다음 ▶️"):
        st.session_state.situation = ""
        st.session_state.options = []
        st.session_state.step = 5
        st.rerun()

def step_5():
    crisis = {
        "📉 원화 급락": ["환 헤지", "수출 확대", "정부 협력"],
        "🇺🇸 기준금리 인상": ["자산 조정", "긴축 경영", "내수 집중"]
    }
    best = {"📉 원화 급락": "환 헤지", "🇺🇸 기준금리 인상": "자산 조정"}
    if not st.session_state.crisis_situation:
        st.session_state.crisis_situation, st.session_state.crisis_options = random.choice(list(crisis.items()))
    show_speech("“국가적 위기 발생!”", st.session_state.crisis_situation, img)
    selected = st.radio("대응 전략 선택", st.session_state.crisis_options)
    if st.button("전략 확정"):
        st.session_state.selected_strategy = selected
        st.session_state.score += 10 if selected == best[st.session_state.crisis_situation] else 5
        st.session_state.crisis_situation = ""
        st.session_state.crisis_options = []
        st.session_state.step = 6
        st.rerun()

def step_6():
    score = st.session_state.score
    if score >= 20:
        show_speech("“최고의 경영자군!”", f"최종 점수: {score}", img)
    else:
        show_speech("“아직 갈 길이 남았군.”", f"점수: {score}", img)
    if st.button("다음 ▶️"):
        st.session_state.step = 7
        st.rerun()

def step_7():
    options = {"🧠 조직문화 혁신": 10, "💰 복지 강화": 8, "📚 교육 강화": 7, "🧘 무대응": 2}
    show_speech("“내부 갈등 발생!”", "직원 사기 저하, 어떻게 할까?", img)
    selected = st.radio("전략 선택", list(options.keys()))
    if st.button("전략 확정"):
        st.session_state.selected_strategy = selected
        st.session_state.score += options[selected]
        st.session_state.step = 8
        st.rerun()

def step_8():
    events = {
        "📉 글로벌 불황": (["내수 강화", "비용 절감", "시장 철수"], "내수 강화"),
        "🚀 경쟁사 혁신": (["기술 개발", "가격 인하", "마케팅"], "기술 개발")
    }
    if not st.session_state.event_8:
        event, (opts, best) = random.choice(list(events.items()))
        st.session_state.event_8 = event
        st.session_state.event_8_options = opts
        st.session_state.event_8_best = best
    show_speech("“돌발 변수 발생!”", st.session_state.event_8, img)
    selected = st.radio("전략 선택", st.session_state.event_8_options)
    if st.button("전략 확정"):
        st.session_state.selected_strategy = selected
        st.session_state.score += 10 if selected == st.session_state.event_8_best else 5
        st.session_state.step = 9
        st.rerun()

# ✅ 이미지 설정
img = "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png"
event_img = "https://raw.githubusercontent.com/dddowobbb/simulator1/main/badevent.png"

# ✅ 스타일 적용
apply_custom_style()

# ✅ Step 실행
steps = {
    0: step_0,
    1: step_1,
    2: step_2,
    3: step_3,
    4: step_4,
    5: step_5,
    6: step_6,
    7: step_7,
    8: step_8
}
steps.get(st.session_state.step, lambda: st.write("게임 종료"))()
