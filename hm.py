import streamlit as st
import matplotlib.pyplot as plt
import datetime
import time

st.set_page_config(page_title="📚 공부 도우미", layout="centered")

st.title("✨ 공부 도우미 앱 ✨")
st.write("귀엽고 이쁘게 공부를 관리할 수 있는 앱이에요 🐰💡")

# ------------------ 오늘의 공부 목표 ------------------
st.subheader("🎯 오늘의 공부 목표")
if "goals" not in st.session_state:
    st.session_state.goals = []

new_goal = st.text_input("오늘의 목표를 입력하세요 ✍️")
if st.button("목표 추가") and new_goal:
    st.session_state.goals.append({"text": new_goal, "done": False})

for i, goal in enumerate(st.session_state.goals):
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        done = st.checkbox("", value=goal["done"], key=f"goal_{i}")
        st.session_state.goals[i]["done"] = done
    with col2:
        st.write(goal["text"])

# ------------------ 공부 타이머 ------------------
st.subheader("⏰ 공부 타이머 (Pomodoro)")
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False
    st.session_state.timer_start = None
    st.session_state.timer_mode = "공부"

study_time = 25 * 60  # 25분
break_time = 5 * 60   # 5분

if st.button("▶️ 타이머 시작"):
    st.session_state.timer_running = True
    st.session_state.timer_start = time.time()
    st.session_state.timer_mode = "공부"

if st.button("⏹️ 타이머 정지"):
    st.session_state.timer_running = False

if st.session_state.timer_running:
    elapsed = int(time.time() - st.session_state.timer_start)
    duration = study_time if st.session_state.timer_mode == "공부" else break_time
    remaining = duration - elapsed

    if remaining <= 0:
        st.session_state.timer_mode = "휴식" if st.session_state.timer_mode == "공부" else "공부"
        st.session_state.timer_start = time.time()
        st.success(f"{st.session_state.timer_mode} 시간 시작! ✨")
    else:
        mins, secs = divmod(remaining, 60)
        st.info(f"{st.session_state.timer_mode} 시간: {mins:02d}:{secs:02d}")

# ------------------ 공부 시간 기록 ------------------
st.subheader("📈 학습 진도표")
if "study_log" not in st.session_state:
    st.session_state.study_log = {}

add_hours = st.number_input("오늘 공부한 시간을 입력하세요 (시간 단위)", 0.0, 24.0, 1.0, 0.5)
if st.button("공부 시간 기록하기"):
    today = datetime.date.today().strftime("%Y-%m-%d")
    if today not in st.session_state.study_log:
        st.session_state.study_log[today] = 0
    st.session_state.study_log[today] += add_hours
    st.success("기록 완료! ✨")

if st.session_state.study_log:
    dates = list(st.session_state.study_log.keys())
    hours = list(st.session_state.study_log.values())

    fig, ax = plt.subplots()
    ax.plot(dates, hours, marker="o", linestyle="-", linewidth=2)
    ax.set_title("📊 공부 시간 추이")
    ax.set_xlabel("날짜")
    ax.set_ylabel("공부 시간 (h)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.write("---")
st.write("✨ 오늘도 화이팅! 🐥📖")
