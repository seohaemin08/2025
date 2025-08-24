import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time
import random

st.set_page_config(page_title="📚 스마트 공부 도우미", layout="wide")
st.markdown("<h1 style='text-align:center;color:#FF69B4;'>✨ 스마트 공부 도우미 🐥🌸</h1>", unsafe_allow_html=True)

# -----------------------
# 1. 공부 기록 관리
# -----------------------
if "study_log" not in st.session_state:
    st.session_state.study_log = []

st.header("📝 오늘의 공부 기록 입력")
col1, col2 = st.columns(2)
with col1:
    subject = st.text_input("📚 과목")
with col2:
    hours = st.number_input("⏱ 공부 시간 (시간)", min_value=0.0, step=0.5)

if st.button("💾 기록 저장"):
    if subject and hours > 0:
        st.session_state.study_log.append({
            "날짜": datetime.date.today().strftime("%Y-%m-%d"),
            "과목": subject,
            "시간": hours
        })
        st.success("기록이 저장되었습니다! 🎉")

if st.session_state.study_log:
    df = pd.DataFrame(st.session_state.study_log)
    st.subheader("📊 공부 기록")
    st.dataframe(df)

    st.subheader("📈 과목별 총 공부 시간")
    fig, ax = plt.subplots()
    df.groupby("과목")["시간"].sum().plot(kind="bar", ax=ax, color="#FF69B4")
    ax.set_ylabel("총 공부 시간 (시간)")
    st.pyplot(fig)
else:
    st.info("📌 아직 기록이 없습니다. 오늘부터 시작해보세요!")

# -----------------------
# 2. 시험 대비 분석
# -----------------------
if st.session_state.study_log:
    st.header("📖 시험 대비")
    subjects = df["과목"].unique()
    exam_subj = st.selectbox("시험 대비 과목 선택", subjects)
    total_time = df[df["과목"]==exam_subj]["시간"].sum()
    st.write(f"총 공부 시간: {total_time}시간")
    if total_time < 2:
        st.warning("⚠️ 공부 시간이 부족해요!")
    else:
        st.success("💯 충분히 준비되고 있어요!")

# -----------------------
# 3. 과목 비중 분석
# -----------------------
if st.session_state.study_log:
    st.header("🎨 과목 비중 분석")
    fig2, ax2 = plt.subplots()
    subject_time = df.groupby("과목")["시간"].sum()
    colors = ["#FFC0CB", "#FFB6C1", "#FF69B4", "#FF1493", "#FF82A9"]
    ax2.pie(subject_time, labels=subject_time.index, autopct="%1.1f%%", startangle=90, colors=colors)
    ax2.axis("equal")
    st.pyplot(fig2)

# -----------------------
# 4. 집중도 & 피로도 기록
# -----------------------
st.header("🧠 집중도 & 피로도")
if "status_log" not in st.session_state:
    st.session_state.status_log = []

col1, col2 = st.columns(2)
with col1:
    focus = st.slider("🤓 집중도 (1~5)", 1, 5, 3)
with col2:
    fatigue = st.slider("😵 피로도 (1~5)", 1, 5, 3)

if st.button("상태 기록"):
    st.session_state.status_log.append({
        "날짜": datetime.date.today().strftime("%Y-%m-%d"),
        "집중도": focus,
        "피로도": fatigue
    })
    st.success("상태가 기록되었습니다!")

if st.session_state.status_log:
    df_status = pd.DataFrame(st.session_state.status_log)
    st.line_chart(df_status.set_index("날짜"))

# -----------------------
# 5. 오늘 목표 체크리스트
# -----------------------
st.header("✅ 오늘의 목표")
if "goals" not in st.session_state:
    st.session_state.goals = []

new_goal = st.text_input("✍️ 새로운 목표 추가")
if st.button("목표 추가") and new_goal:
    st.session_state.goals.append({"text": new_goal, "done": False})

for i, goal in enumerate(st.session_state.goals):
    checked = st.checkbox(goal["text"], value=goal["done"], key=f"goal_{i}")
    st.session_state.goals[i]["done"] = checked

if st.session_state.goals:
    done_count = sum(g["done"] for g in st.session_state.goals)
    total = len(st.session_state.goals)
    percent = int((done_count/total)*100)
    st.progress(percent)
    st.write(f"🎯 목표 달성률: {done_count}/{total} ({percent}%)")
    if percent == 100:
        st.success("🏆 오늘의 열공왕! 전부 달성했어요! ✨")

# -----------------------
# 6. Pomodoro 타이머
# -----------------------
st.header("⏱️ Pomodoro 타이머")

def pomodoro_timer(minutes, label):
    st.write(f"▶ {label} 시작! ({minutes}분)")
    progress_bar = st.progress(0)
    for sec in range(minutes*6):  # 테스트용 10초 단위
        time.sleep(0.1)
        progress_bar.progress(int((sec+1)/(minutes*6)*100))
    st.success(f"✅ {label} 종료!")

if st.button("Pomodoro 시작"):
    pomodoro_timer(25, "공부")
    pomodoro_timer(5, "휴식")
