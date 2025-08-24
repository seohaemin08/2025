import streamlit as st
import pandas as pd
import time
from datetime import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="📚 스마트 공부 도우미", layout="wide")

st.title("📚 AI 기반 스마트 공부 도우미")
st.markdown("인공지능학과 진로를 위한 **공부 관리 + 분석 시스템** ✨")

# -----------------------
# 1. 공부 목표 기록
# -----------------------
st.header("📝 공부 목표 기록")
subject = st.text_input("과목 입력")
goal = st.text_input("공부 목표 입력")
time_spent = st.number_input("공부한 시간 (분)", min_value=0)

if "study_log" not in st.session_state:
    st.session_state.study_log = []

if st.button("기록 추가"):
    if subject and goal and time_spent > 0:
        st.session_state.study_log.append({
            "과목": subject,
            "목표": goal,
            "시간": time_spent,
            "날짜": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        st.success("✅ 기록이 추가되었습니다!")

if st.session_state.study_log:
    df = pd.DataFrame(st.session_state.study_log)
    st.dataframe(df)

    # 시각화
    st.subheader("📊 과목별 공부 시간")
    subject_time = df.groupby("과목")["시간"].sum()
    fig, ax = plt.subplots()
    subject_time.plot(kind="bar", ax=ax)
    ax.set_ylabel("총 공부 시간(분)")
    st.pyplot(fig)

# -----------------------
# 2. 시험 대비 분석
# -----------------------
st.header("📖 시험 대비")
exam_subject = st.selectbox("시험 대비 과목 선택", options=[s["과목"] for s in st.session_state.study_log] if st.session_state.study_log else [])
if exam_subject:
    study_time = sum([s["시간"] for s in st.session_state.study_log if s["과목"] == exam_subject])
    st.write(f"📌 **{exam_subject}** 과목 총 공부 시간: {study_time}분")
    if study_time < 120:
        st.warning("⚠️ 공부 시간이 부족해요! 시간을 늘리세요.")
    else:
        st.success("💯 충분히 준비되고 있어요!")

# -----------------------
# 3. 과목 비중 분석
# -----------------------
if st.session_state.study_log:
    st.header("📊 과목 비중 분석")
    fig2, ax2 = plt.subplots()
    ax2.pie(subject_time, labels=subject_time.index, autopct="%1.1f%%", startangle=90)
    ax2.set_title("과목별 공부 비중")
    st.pyplot(fig2)

# -----------------------
# 4. 집중도 & 피로도 기록
# -----------------------
st.header("🧠 집중도 & 피로도 분석")
focus = st.slider("오늘의 집중도 (1-10)", 1, 10, 5)
tired = st.slider("오늘의 피로도 (1-10)", 1, 10, 5)

if "status_log" not in st.session_state:
    st.session_state.status_log = []

if st.button("상태 기록"):
    st.session_state.status_log.append({
        "날짜": datetime.now().strftime("%Y-%m-%d"),
        "집중도": focus,
        "피로도": tired
    })
    st.success("🧾 상태가 기록되었습니다!")

if st.session_state.status_log:
    df_status = pd.DataFrame(st.session_state.status_log)
    st.line_chart(df_status.set_index("날짜"))

# -----------------------
# 5. 오늘 목표 체크리스트
# -----------------------
st.header("✅ 오늘의 공부 목표")
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
st.header("⏱️ Pomodoro 공부 타이머")

def pomodoro_timer(minutes, label):
    st.write(f"▶ {label} 시작! ({minutes}분)")
    progress_bar = st.progress(0)
    for sec in range(minutes * 6):  # 10초 단위 (테스트용 빠르게 진행)
        time.sleep(0.1)
        progress_bar.progress(int((sec+1)/(minutes*6)*100))
    st.success(f"✅ {label} 종료!")

if st.button("Pomodoro 시작 (25분 공부 / 5분 휴식)"):
    pomodoro_timer(25, "공부")
    pomodoro_timer(5, "휴식")
