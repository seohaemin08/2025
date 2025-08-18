import streamlit as st

# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기 🎀✨", page_icon="💖", layout="centered")

# 🎉 타이틀
st.title("🌟 MBTI 기반 직업 추천 사이트 💼✨")
st.markdown("""
💖 안녕하세요! 귀엽고 화려한 🌸 MBTI 진로 추천기 🌸에 오신 것을 환영합니다!

👉 MBTI를 선택하면, 당신에게 딱 맞는 직업을 추천해드릴게요! 🐰🎀
""")

# 📝 MBTI 리스트
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 🧸 MBTI별 직업 추천 데이터
mbti_jobs = {
    "ISTJ": "📊 회계사, 🏦 은행원, 📚 사서",
    "ISFJ": "👩‍🏫 교사, 🏥 간호사, 🧸 사회복지사",
    "INFJ": "🎨 예술가, 📝 작가, 🧑‍🏫 상담가",
    "INTJ": "🧠 과학자, 💻 데이터 분석가, 🛰 연구원",
    "ISTP": "🔧 엔지니어, 🚗 정비사, 🕹 게임 개발자",
    "ISFP": "🎶 음악가, 🎨 디자이너, 🌿 플로리스트",
    "INFP": "📝 시인, 🎭 배우, 🌍 NGO 활동가",
    "INTP": "💻 프로그래머, 🧠 연구원, 🛰 발명가",
    "ESTP": "📈 영업가, 🎤 방송인, ⚽ 운동선수",
    "ESFP": "🎶 가수, 🎭 배우, 🎉 이벤트 플래너",
    "ENFP": "🌍 여행가, 🧑‍🎤 크리에이터, 📢 마케터",
    "ENTP": "💡 기업가, 🎤 토론가, 🚀 스타트업 CEO",
    "ESTJ": "📊 관리자, 🏢 경영자, 🛠 프로젝트 매니저",
    "ESFJ": "👩‍🏫 교사, 🤝 상담사, 🏥 의료 서비스",
    "ENFJ": "🎤 연설가, 📢 마케터, 🧑‍🏫 멘토",
    "ENTJ": "🚀 CEO, 📈 투자자, 🧠 전략 컨설턴트"
}

# 💖 사용자 입력
st.subheader("✨ 당신의 MBTI를 선택해주세요! 🐰💼")
user_mbti = st.selectbox("👉 MBTI를 골라주세요:", mbti_list, index=0)

# 🎀 추천 결과 출력
if user_mbti:
    st.markdown(f"""
    ## 🎉 당신의 MBTI: **{user_mbti}** 🌟

    🐣 추천 직업은 바로바로... 💖 

    👉 {mbti_jobs[user_mbti]} ✨✨

    🌸 당신의 미래는 반짝반짝 빛날 거예요! 🌟🌈💼
    """)

# 🐰 하단 귀여운 멘트
st.markdown("""
---
🌷 제작자: **당신의 AI 친구 🤖💖**

✨ 오늘도 반짝이는 하루 되세요! 🐰🌸🌈
""")

