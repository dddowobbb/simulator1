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
div[data-baseweb="select"] * {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

# ✅ 말풍선 함수

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
    show_speech("“환영합니다!”", "게임 시작 전에 준비하세요!", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    if st.button("게임 시작 ▶️"):
        st.session_state.step = 1
        st.rerun()

# ✅ Step 1: 업종 선택
elif st.session_state.step == 1:
    industries = ["💻 IT 스타트업", "🌱 친환경 제품", "🎮 게임 개발사", "👗 패션 브랜드", "🍔 푸드테크", "🛒 글로벌 전자상거래"]
    if not st.session_state.industry_confirmed:
        show_speech("“산업을 선택하자.”", "우리는 어떤 분야에서 시작할까?", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
        selected = st.selectbox("회사 업종을 선택해주세요", industries)
        if st.button("업종 확정"):
            st.session_state.industry = selected
            st.session_state.industry_confirmed = True
            st.session_state.step = 2
            st.rerun()

# ✅ Step 2: 회사 이름
elif st.session_state.step == 2:
    show_speech("“이제 회사를 설립할 시간이야.”", "멋진 회사 이름을 지어보자!", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    name = st.text_input("당신의 회사 이름은?")
    if st.button("회사 이름 확정"):
        if name.strip():
            st.session_state.company_name = name.strip()
            st.session_state.step = 3
            st.rerun()

# ✅ Step 3: 위기 상황
elif st.session_state.step == 3:
    situations = {
        "📉 매출 급감": ["광고 강화", "신제품 출시", "가격 인하"],
        "🔥 경쟁사 파산": ["인재 영입", "시장 확대", "기술 인수"]
    }
    if not st.session_state.situation:
        st.session_state.situation, st.session_state.options = random.choice(list(situations.items()))

    show_speech("“문제가 발생했어!”", st.session_state.situation, "https://raw.githubusercontent.com/dddowobbb/simulator1/main/badevent.png")
    choice = st.radio("전략 선택", st.session_state.options)
    if st.button("전략 확정"):
        st.session_state.selected_strategy = choice
        st.session_state.score += 10
        st.session_state.step = 4
        st.rerun()

# ✅ Step 4: 결과 피드백
elif st.session_state.step == 4:
    show_speech("전략 결과!", f"{st.session_state.selected_strategy} 전략 점수 +10", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    st.session_state.step = 5
    st.rerun()

# ✅ Step 5: 국가 위기
elif st.session_state.step == 5:
    crisis = {
        "💸 외환 위기": ["환 헤지", "수출 확대"],
        "🗳️ 대통령 탄핵": ["리스크 분산", "정치 모니터링"]
    }
    if not st.session_state.crisis_situation:
        st.session_state.crisis_situation, st.session_state.crisis_options = random.choice(list(crisis.items()))

    show_speech("국가 위기 발생", st.session_state.crisis_situation, "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    strategy = st.radio("대응 전략", st.session_state.crisis_options)
    if st.button("전략 확정"):
        st.session_state.selected_strategy = strategy
        st.session_state.score += 10
        st.session_state.step = 6
        st.rerun()

# ✅ Step 6: 피드백
elif st.session_state.step == 6:
    show_speech("전략 결과", f"{st.session_state.selected_strategy} 선택 → 점수 +10", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    st.session_state.step = 7
    st.rerun()

# ✅ Step 7: 내부 문제
elif st.session_state.step == 7:
    issues = {
        "🧠 조직문화 혁신": 10,
        "💰 복지 강화": 8,
        "🔁 리더십 교체": 6,
        "📚 교육 강화": 7
    }
    show_speech("내부 문제 발생", "사기 저하, 인사 갈등 등", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    selected = st.radio("해결 전략을 선택하세요:", list(issues.keys()))
    if st.button("전략 확정"):
        st.session_state.selected_strategy = selected
        st.session_state.score += issues[selected]
        st.session_state.step = 8
        st.rerun()

# ✅ Step 8: 성장 전략
elif st.session_state.step == 8:
    strategies = {
        "📢 광고 집중": ["IT 스타트업", "게임 개발사"],
        "🌍 해외 진출": ["글로벌 전자상거래"],
        "🤝 M&A": ["친환경 제품"],
        "💲 가격 인하": ["패션 브랜드"],
        "👑 프리미엄 전략": ["푸드테크"]
    }
    show_speech("제품 인기도 상승", "성장 전략을 결정하세요", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    selected = st.radio("전략 선택", list(strategies.keys()))
    if st.button("전략 확정"):
        field = st.session_state.industry.split()[-1]
        score = 10 if field in strategies[selected] else 5
        st.session_state.selected_strategy = selected
        st.session_state.score += score
        st.session_state.step = 9
        st.rerun()

# ✅ Step 9: 리포트
elif st.session_state.step == 9:
    show_speech("3년간 리포트", f"총 점수: {st.session_state.score}", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    st.markdown(f"### 📊 리포트 요약\n- 시장 점유율: {'🔺' if st.session_state.score > 40 else '🔻'}\n- 브랜드 평판: {'좋음' if st.session_state.score > 40 else '보통'}\n- 직원 만족도: {'높음' if st.session_state.score > 35 else '낮음'}")
    st.session_state.step = 10
    st.rerun()

# ✅ Step 10: 최종 평가
elif st.session_state.step == 10:
    if st.session_state.score >= 50:
        msg = "★★★★☆ 글로벌 유니콘 기업 달성!"
    elif st.session_state.score >= 30:
        msg = "★★★☆☆ 안정적 성장"
    else:
        msg = "★★☆☆☆ 존폐 위기의 스타트업"
    show_speech("최종 평가", msg, "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    st.balloons()
    st.markdown(f"### 🏁 당신의 최종 점수: {st.session_state.score}점")
