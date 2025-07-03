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

/* ✅ selectbox 내부 텍스트는 검정색 */
.stSelectbox div[role="option"] {
    color: #000000 !important;
}
.stSelectbox > div > div > div {
    color: #000000 !important;
}

/* (나머지 말풍선, 배경, 등은 동일하게 유지) */
...
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
