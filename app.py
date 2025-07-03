import streamlit as st

# Step 1: 초기 세션 설정
if "step" not in st.session_state:
    st.session_state.step = 1
if "industry" not in st.session_state:
    st.session_state.industry = ""
if "industry_confirmed" not in st.session_state:
    st.session_state.industry_confirmed = False

# ✅ 전체 글씨 색상 하얗게 만드는 CSS + UI 스타일
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
}
h1, h2, h3, h4, h5, h6, label, p, span, div {
    color: #ffffff !important;
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

st.markdown("""
<style>
/* ✅ selectbox 내부 텍스트는 검정색 */
.stSelectbox div[data-baseweb="select"] * {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

# 말풍선 대사 설정
def get_step1_speech():
    if not st.session_state.industry_confirmed:
        return "“좋아, 이제 우리가 어떤 산업에 뛰어들지 결정할 시간이군.”", "어떤 분야에서 승부할지, 네 선택을 보여줘."
    else:
        return f"“{st.session_state.industry}... 흥미로운 선택이군.”", "다음 단계로 가볼까?"

title, subtitle = get_step1_speech()

# 말풍선 및 배경
st.markdown(f"""
<div class="container">
    <img class="bg-image" src="https://raw.githubusercontent.com/dddowobbb/16-1/main/talking%20ceo.png" />
    <div class="speech-bubble">
        <div class="speech-title">{title}</div>
        <div class="speech-sub">{subtitle}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 📍 1단계 본문: 회사 분야 선택
st.markdown("### Step 1: 회사 분야 선택")

industries = ["💻 IT 스타트업", "🌱 친환경 제품", "🎮 게임 개발사", "👗 패션 브랜드", "🍔 푸드테크", "🛒 글로벌 전자상거래"]

if not st.session_state.industry_confirmed:
    selected = st.selectbox("회사 업종을 선택해주세요", industries)
    if st.button("업종 확정"):
        st.session_state.industry = selected
        st.session_state.industry_confirmed = True
        st.session_state.step = 2  # ✅ 다음 단계로 이동
        st.rerun()
else:
    st.success(f"✅ 선택된 업종: {st.session_state.industry}")
