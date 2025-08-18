import streamlit as st
import pandas as pd
import random

# 페이지 설정
st.set_page_config(page_title="AI 공부 플래너", page_icon="🐰", layout="centered")

# 상단 배너
st.markdown(
    """
    <div style="text-align:center;">
        <h1>🐰✨ AI 기반 공부 플래너 ✨📚</h1>
        <p>공부를 더 귀엽고 즐겁게! <br> 나만의 공부 계획표를 만들어봐요 💖</p>
        <img src="https://cdn-icons-png.flaticon.com/512/4341/4341053.png" width="120">
    </div>
    """,
    unsafe_allow_html=True
)

# 사용자 입력
subjects = st.text_input("📚 공부할 과목을 입력하세요 (쉼표로 구분)", "수학, 영어, 과학")
hours_per_day = st.slider("⏰ 하루 공부 가능 시간", 1, 12, 4)
days = st.slider("📅 계획할 기간(일)", 1, 30, 7)
intensity = st.radio("🔥 공부 강도", ["🐢 가볍게", "🐥 보통", "🐯 집중"])

if st.button("✨ 나만의 공부 계획 만들기 ✨"):
    # 임시 시간 배분 (랜덤 요소 추가)
    subj_list = [s.strip() for s in subjects.split(",")]
    time_alloc = [random.randint(1, hours_per_day) for _ in subj_list]
    total = sum(time_alloc)
    time_alloc = [round(t * hours_per_day / total, 1) for t in time_alloc]

    # 계획표 생성 (예시)
    plan = f"""
    🌸 **{days}일 공부 계획표** 🌸  
    하루 {hours_per_day}시간 동안 공부할 거예요!  
    강도는 {intensity} 모드 💪  
    """
    st.markdown(plan)

    # 카드 스타일 출력
    for subj, t in zip(subj_list, time_alloc):
        st.markdown(
            f"""
            <div style="background-color:#ffe6f2;
                        border-radius:20px;
                        padding:15px;
                        margin:10px 0;
                        box-shadow:2px 2px 5px #ffb3d9;">
                <h3>📖 {subj} : {t}시간</h3>
                <p>✨ 오늘도 화이팅 ✨</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 귀여운 차트
    df = pd.DataFrame({
        "과목": subj_list,
        "시간": time_alloc
    })
    st.bar_chart(df.set_index("과목"))

    # 하단 귀여운 이미지
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=100)
    st.success("🐰 공부 계획이 완성되었어요! 오늘도 파이팅 🐰")

