import streamlit as st

# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기 🎀✨", page_icon="💖", layout="centered")

# 🌸 배경 색상 CSS
page_bg_css = """
<style>
body {
    background-color: #ffe6f2;
}
.tarot-card {
    background: linear-gradient(135deg, #fff0f6, #ffe6f2);
    border: 4px solid #ff99cc;
    border-radius: 25px;
    padding: 30px;
    width: 300px;
    margin: 30px auto;
    text-align: center;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.tarot-card:hover {
    transform: rotate(-2deg) scale(1.05);
    box-shadow: 0px 12px 25px rgba(0,0,0,0.3);
}
.tarot-title {
    font-size: 24px;
    color: #cc0066;
    margin-bottom: 10px;
}
.tarot-job {
    font-size: 20px;
    color: #660033;
    margin-top: 15px;
}
</style>
"""

st.markdown(page_bg_css, unsafe_allow_html=True)

# 🎉 타이틀
st.title("🔮 MBTI 타로 진로 추천 💼✨")
st.markdown("""
💖 안녕하세요! 🌸 MBTI 타로 진로 추천 🌸에 오신 것을 환영합니다!

👉 MBTI를 선택하면, 타로카드처럼 ✨당신의 직업 운명✨을 알려드려요! 🐰🎀
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

# 🎀 추천 결과 타로카드 형식 출력
if user_mbti:
    st.markdown(f"""
    <div class="tarot-card">
        <div class="tarot-title">🔮 당신의 MBTI: <b>{user_mbti}</b> 🌟</div>
        <p>🐣 운명처럼 다가온 직업은... 💖</p>
        <div class="tarot-job">{mbti_jobs[user_mbti]} ✨</div>
        <p>🌸 당신의 미래는 반짝반짝 빛날 거예요! 🌟🌈💼</p>
    </div>
    """, unsafe_allow_html=True)

# 🐰 하단 귀여운 멘트
st.markdown("""
---
🌷 제작자: **당신의 AI 친구 🤖💖**

✨ 오늘도 행운 가득한 하루 되세요! 🐰🔮🌸
""")
