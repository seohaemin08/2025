import streamlit as st
import matplotlib.pyplot as plt
from textblob import TextBlob

st.set_page_config(page_title="AI 감정 분석 일기", layout="centered")

st.title("📔 AI 기반 감정 분석 일기 앱")

# 1. 일기 입력
diary = st.text_area("오늘 하루를 기록해보세요:")

if st.button("감정 분석 시작"):
    if diary.strip() == "":
        st.warning("✍️ 일기를 입력해주세요.")
    else:
        # 2. 감정 분석
        blob = TextBlob(diary)
        polarity = blob.sentiment.polarity  # -1 ~ 1
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            emotion = "😊 긍정적"
        elif polarity < 0:
            emotion = "😢 부정적"
        else:
            emotion = "😐 중립적"

        st.subheader("🧠 감정 분석 결과")
        st.write(f"감정: {emotion}")
        st.write(f"긍정/부정 지수 (Polarity): {polarity:.2f}")
        st.write(f"주관성 (Subjectivity): {subjectivity:.2f}")

        # 3. 시각화
        labels = ["부정", "중립", "긍정"]
        sizes = [max(0, -polarity), 1-abs(polarity), max(0, polarity)]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

        # 4. 추천
        st.subheader("🎵 맞춤 추천")
        if polarity > 0.2:
            st.write("🌟 오늘은 기분이 좋네요! → 신나는 음악: BTS - Dynamite 🎶")
            st.write("🍿 영화 추천: 인사이드 아웃 2")
        elif polarity < -0.2:
            st.write("💙 힘든 하루였군요. → 위로되는 음악: Paul Kim - 모든 날, 모든 순간 🎶")
            st.write("🍿 영화 추천: 월터의 상상은 현실이 된다")
        else:
            st.write("🌤 잔잔한 하루였군요. → 편안한 음악: IU - 밤편지 🎶")
            st.write("🍿 영화 추천: 리틀 포레스트")
