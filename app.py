import streamlit as st

# ✅ 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 1
if "industry" not in st.session_state:
    st.session_state.industry = ""
if "industry_confirmed" not in st.session_state:
    st.session_state.industry_confirmed = False
if "company_name" not in st.session_state:
    st.session_state.company_name = ""

# ✅ 스타일 (배경 + 글씨색 + selectbox + 버튼)
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
}
h1, h2, h3, h4, h5, h6, label, p, span, div {
    color: #ffffff !important;
}
.stSelectbox div[data-baseweb="select"] * {
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

# ✅ 말풍선 생성 함수
def show_speech(title, subtitle):
    st.markdown(f"""
    <div class="container">
        <img class="bg-image" src="https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png" />
        <div class="speech-bubble">
            <div class="speech-title">{title}</div>
            <div class="speech-sub">{subtitle}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ✅ Step 1: 업종 선택
if st.session_state.step == 1:
    if not st.session_state.industry_confirmed:
        show_speech("“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”", "어떤 분야에서 승부할지, 네 선택을 보여줘.")
    else:
        show_speech(f"“{st.session_state.industry}... 흥미로운 선택이군.”", "다음 단계로 가볼까?")

    st.markdown("### Step 1: 회사 분야 선택")
    industries = ["💻 IT 스타트업", "🌱 친환경 제품", "🎮 게임 개발사", "👗 패션 브랜드", "🍔 푸드테크", "🛒 글로벌 전자상거래"]

    if not st.session_state.industry_confirmed:
        selected = st.selectbox("회사 업종을 선택해주세요", industries)
        if st.button("업종 확정"):
            st.session_state.industry = selected
            st.session_state.industry_confirmed = True
            st.session_state.step = 2
            st.rerun()
    else:
        st.success(f"✅ 선택된 업종: {st.session_state.industry}")
        if st.button("다음 ▶️"):
            st.session_state.step = 2
            st.rerun()

# ✅ Step 2: 회사 이름 입력
elif st.session_state.step == 2:
    if not st.session_state.company_name:
        show_speech("“이제 회사를 설립할 시간이야.”", "멋진 회사 이름을 지어보자!")
    else:
        show_speech(f"“{st.session_state.company_name}... 멋진 이름이군!”", "이제 다음 단계로 넘어가자.")

    st.markdown("### Step 2: 회사 이름 입력")
    name_input = st.text_input("당신의 회사 이름은?", max_chars=20)

    if st.button("회사 이름 확정"):
        if name_input.strip():
            st.session_state.company_name = name_input.strip()
            st.success("✅ 회사 이름이 등록되었습니다!")
        else:
            st.warning("⚠️ 회사 이름을 입력해주세요.")

    if st.session_state.company_name and st.button("다음 ▶️"):
        st.session_state.step = 3
        st.rerun


import streamlit as st
import random

# ✅ Step 3 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = 3
if "score" not in st.session_state:
    st.session_state.score = 0
if "history" not in st.session_state:
    st.session_state.history = []

# ✅ Step 3 화면: 돌발 이벤트 발생
if st.session_state.step == 3:

    # 최적 전략 매핑
    effective_strategies = {
        "⚠️ 대규모 고객 정보 유출": "보안 시스템 전면 재구축",
        "📈 갑작스러운 수요 폭증": "생산 라인 증설",
        "💸 원자재 가격 급등": "공급처 다변화",
        "🔥 경쟁사 파산": "인재 채용 강화",
        "🏆 글로벌 시장 진출 기회": "현지화 전략"
    }

    # 랜덤 상황 선택
    situation, options = random.choice([
        ("⚠️ 대규모 고객 정보 유출", ["보안 시스템 전면 재구축", "사과문 발표", "내부 책임자 교체", "조용히 넘어감", "보험 청구"]),
        ("📈 갑작스러운 수요 폭증", ["생산 라인 증설", "가격 인상", "예약 판매", "품절 마케팅", "신규 고용"]),
        ("💸 원자재 가격 급등", ["공급처 다변화", "생산 중단", "재고 우선 소비", "소비자 가격 인상", "대체 원료 탐색"]),
        ("🔥 경쟁사 파산", ["인재 채용 강화", "시장 점유율 확대", "해당 기업 인수", "광고 강화", "신제품 발표"]),
        ("🏆 글로벌 시장 진출 기회", ["현지화 전략", "글로벌 광고 캠페인", "온라인 직판", "외국 파트너와 제휴", "해외 공장 설립"])
    ])

    # ✅ 스타일
    st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
    }
    h1, h2, h3, h4, h5, h6, label, p, span, div {
        color: #ffffff !important;
    }
    .stSelectbox div[data-baseweb="select"] * {
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

    # ✅ 말풍선 + 배경 이미지 출력
    st.markdown(f"""
    <div class="container">
        <img class="bg-image" src="https://raw.githubusercontent.com/dddowobbb/16-1/main/unexpected_event.png" />
        <div class="speech-bubble">
            <div class="speech-title">“예기치 못한 사건 발생!”</div>
            <div class="speech-sub">상황에 적절한 전략을 선택해 회사를 지켜내자.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ✅ 본문 영역
    st.markdown("### Step 3: 전략 선택")
    st.markdown(f"#### 📍 상황: {situation}")
    selected = st.radio("🧠 당신의 전략은?", options)

    if st.button("전략 확정"):
        if selected == effective_strategies.get(situation):
            st.session_state.score += 10
        else:
            st.session_state.score += 5

        st.session_state.history.append((situation, selected))
        st.session_state.step = 4
        st.rerun()
