import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
import os
from datetime import datetime

# CSV 파일 이름
CSV_FILE = "study_log.csv"

# 랜덤 응원 문구 리스트
encouragements = [
    "대단해요! 오늘도 목표를 향해 한 걸음 나아갔어요 🚀",
    "노력은 절대 배신하지 않아요. 화이팅! 💪",
    "작은 성취가 큰 변화를 만듭니다 🌱",
    "오늘도 스스로를 칭찬해주세요 👏",
    "당신의 꾸준함이 곧 성공의 열쇠예요 🔑",
    "넘어져도 다시 일어나면 돼요! 계속 전진하세요 🏃",
    "당신은 이미 멋진 길을 걷고 있어요 🌟"
]

# CSV 파일 초기화
def init_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["날짜", "과목", "공부시간(분)"])
        df.to_csv(CSV_FILE, index=False)

# 공부 기록 저장
def save_study_log(subject, minutes):
    date = datetime.now().strftime("%Y-%m-%d")
    new_data = pd.DataFrame([[date, subject, minutes]], columns=["날짜", "과목", "공부시간(분)"])
    df = pd.read_csv(CSV_FILE)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

# 공부 기록 불러오기
def load_study_log():
    return pd.read_csv(CSV_FILE)

# Streamlit 앱 실행
st.title("📚 나만의 공부 기록 앱")

# CSV 초기화
init_csv()

# ✅ 오늘 목표 체크리스트 입력
st.subheader("🎯 오늘 목표 설정")
goals_input = st.text_area("오늘의 목표를 입력하세요 (예: 수학, 영어, 과학)")

if goals_input:
    goals = [g.strip() for g in goals_input.split(",")]
    goal_status = {}
    for g in goals:
        goal_status[g] = st.checkbox(f"{g} 목표 달성 여부")

# 공부 기록 입력
st.subheader("✍ 공부 기록 입력")
subject = st.text_input("과목 이름")
minutes = st.number_input("공부 시간 (분)", min_value=1, step=1)

if st.button("저장하기"):
    if subject and minutes:
        save_study_log(subject, minutes)
        st.success(f"{subject} - {minutes}분 저장 완료!")

# 공부 기록 확인
st.subheader("📊 공부 기록 확인")
log_df = load_study_log()
st.dataframe(log_df)

# 시각화
if not log_df.empty:
    st.subheader("📈 과목별 공부 시간 시각화")
    subject_time = log_df.groupby("과목")["공부시간(분)"].sum()

    fig, ax = plt.subplots()
    subject_time.plot(kind="bar", ax=ax)
    ax.set_ylabel("공부시간(분)")
    ax.set_title("과목별 누적 공부시간")
    st.pyplot(fig)

# ✅ 오늘 목표 달성률 표시 + 랜덤 응원 문구
if goals_input:
    achieved = sum(goal_status.values())
    total = len(goal_status)
    st.subheader("🎉 오늘의 목표 달성률")
    st.write(f"{achieved} / {total} 달성 ({(achieved/total)*100:.1f}%)")

    if achieved == total and total > 0:
        st.success("모든 목표를 달성했어요! 🏆")
    
    st.info(random.choice(encouragements))
