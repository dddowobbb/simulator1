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
    <div class="container">
        <img src="{image_url}" class="bg-image">
        <div class="speech-bubble">
            <div class="speech-title">{title}</div>
            <div class="speech-sub">{subtitle}</div>
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
        st.rerun()

# ✅ Step 1: 업종 선택
elif st.session_state.step == 1:
    if not st.session_state.industry_confirmed:
        show_speech("“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”", "어떤 분야에서 승부할지, 네 선택을 보여줘.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    else:
        show_speech(f"“{st.session_state.industry}... 흥미로운 선택이군.”", "다음 단계로 가볼까?", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")

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
        show_speech("“이제 회사를 설립할 시간이야.”", "멋진 회사 이름을 지어보자!", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")
    else:
        show_speech(f"“{st.session_state.company_name}... 멋진 이름이군!”", "이제 다음 단계로 넘어가자.", "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")

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
        st.rerun()

# ✅ Step 3: 전략 선택
elif st.session_state.step == 3:
    show_speech("“예기치 못한 사건 발생!”", "상황에 적절한 전략을 선택해 회사를 지켜내자.", "https://raw.githubusercontent.com/dddowobbb/simulator1/main/badevent.png")

    situations = {
        "⚠️ 대규모 고객 데이터 유출 발생": ["보안 시스템 전면 재구축", "PR 대응", "사과문 발표", "외부 컨설턴트 투입", "서비스 일시 중단"],
        "📈 갑작스러운 수요 폭증": ["생산 라인 확장", "기술 투자", "임시 고용 확대", "외주 활용", "품질 단가 조정"],
        "💸 원자재 가격 급등": ["공급처 다변화", "대체 소재 도입", "장기 계약", "수입 조정", "원가 절감"],
        "🔥 경쟁사 파산": ["인재 채용 강화", "기술 인수", "시장 확대", "기술 유출 방지", "법적 검토"],
        "📉 주요 제품 매출 급감": ["제품 리뉴얼", "광고 캠페인", "신제품 출시", "할인 행사", "시장 조사"],
        "🏆 대기업으로부터 투자 제안": ["지분 일부 매각", "전략적 제휴", "거절", "조건 재협상", "지분 공동 소유"],
        "🌍 글로벌 시장 진출 기회": ["현지화 전략", "글로벌 광고 캠페인", "온라인 직판", "외국 파트너와 제휴", "해외 공장 설립"]
    }

    if not st.session_state.situation:
        st.session_state.situation, st.session_state.options = random.choice(list(situations.items()))

    st.markdown("### Step 3: 전략 선택")
    st.markdown(f"📍 **상황:** {st.session_state.situation}")
    strategy = st.radio("🧠 당신의 전략은?", st.session_state.options)

    effective_strategies = {
        "⚠️ 대규모 고객 데이터 유출 발생": "보안 시스템 전면 재구축",
        "📈 갑작스러운 수요 폭증": "생산 라인 확장",
        "💸 원자재 가격 급등": "공급처 다변화",
        "🔥 경쟁사 파산": "인재 채용 강화",
        "📉 주요 제품 매출 급감": "제품 리뉴얼",
        "🏆 대기업으로부터 투자 제안": "지분 일부 매각",
        "🌍 글로벌 시장 진출 기회": "현지화 전략"
    }

    if st.button("전략 확정"):
        st.session_state.selected_strategy = strategy
        if strategy == effective_strategies.get(st.session_state.situation):
            st.session_state.score += 10
        else:
            st.session_state.score += 5
        st.session_state.step = 4
        st.rerun()

# ✅ Step 4: 결과 분석 및 피드백
elif st.session_state.step == 4:
    if st.session_state.selected_strategy:
        if st.session_state.score >= 10:
            title = "“훌륭한 판단이었어!”"
            subtitle = f"{st.session_state.selected_strategy} 전략은 최고의 선택이었지. 점수: {st.session_state.score}점"
        else:
            title = "“음... 더 나은 전략도 있었을 거야.”"
            subtitle = f"{st.session_state.selected_strategy} 전략도 나쁘지 않았어. 점수: {st.session_state.score}점"
    else:
        title = "“전략이 필요했는데 말이야...”"
        subtitle = "아무 전략도 선택하지 않았어. 다음엔 신중하게 선택하자."

    show_speech(title, subtitle, "https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png")

    st.markdown("### Step 4: 결과 분석")
    st.success(f"당신의 전략: **{st.session_state.selected_strategy}**")
    st.info(f"현재 점수: **{st.session_state.score}점**")

    if st.button("다음 이벤트 ▶️"):
        st.session_state.situation = ""
        st.session_state.options = []
        st.session_state.selected_strategy = ""
        st.session_state.step = 5
        st.rerun()
# ✅ Step 5: 국가적 위기 대응
elif st.session_state.step == 5:
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
    crisis_strategy = st.radio("🧠 대응 전략을 선택하세요:", st.session_state.crisis_options)

    best_strategies = {
        "📉 한국 외환시장 급변 (원화 가치 급락)": "환 헤지 강화",
        "🇺🇸 미 연준의 기준금리 급등": "고금리 대비 자산 조정",
        "🗳️ 윤석열 대통령 탄핵 가결": "리스크 분산 경영",
        "🇺🇸 트럼프 대선 재당선": "공급망 재편",
        "🛃 주요 국가의 관세 인상 정책": "무역 파트너 다변화"
    }

    if st.button("전략 확정"):
        st.session_state.selected_strategy = crisis_strategy
        if crisis_strategy == best_strategies.get(st.session_state.crisis_situation):
            st.session_state.score += 10
        else:
            st.session_state.score += 5
        st.session_state.crisis_situation = ""
        st.session_state.crisis_options = []
        st.session_state.step = 6
        st.rerun()
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

    col1, col2 = st.columns(2)
    with col1:
        if st.button("다음 ▶️"):
            st.session_state.step = 7
            st.rerun()
    with col2:
        if st.button("게임 다시 시작 🔄"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

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



