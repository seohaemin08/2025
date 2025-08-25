import streamlit as st
import pandas as pd
import random
import datetime

# 세션 상태 초기화
if "plans" not in st.session_state:
    st.session_state.plans = []  # 오늘의 계획
if "logs" not in st.session_state:
    st.session_state.logs = []   # 공부 기록

# 응원 메시지
messages = [
    "너 오늘도 해냈어! 대단하다 👍",
    "계획대로 한 걸 보니 멋지다 💪",
    "꾸준함이 너의 무기야 🌟",
    "조금씩이라도 성장하고 있어 🚀",
    "포기하지 않는 네가 자랑스러워 👏",
    "오늘도 최선을 다한 너에게 박수 👏",
    "내일의 너는 더 성장해 있을 거야 🌱"
]

st.title("📚 AI 스터디 플래너")

tab1, tab2, tab3 = st.tabs(["오늘의 계획", "공부 기록", "주간 통계"])

# -------------------------
# 1. 오늘의 계획
# -------------------------
with tab1:
    st.header("📝 오늘의 계획 세우기")
    subject = st.text_input("과목/주제")
    expected_time = st.number_input("예상 공부 시간(시간)", min_value=0.5, step=0.5)

    if st.button("계획 추가"):
        st.session_state.plans.append({
            "date": datetime.date.today(),
            "subject": subject,
            "expected_time": expected_time,
            "done": False
        })

    st.subheader("📌 오늘의 계획 목록")
    for i, plan in enumerate(st.session_state.plans):
        if plan["date"] == datetime.date.today():
            col1, col2 = st.columns([4,1])
            with col1:
                st.write(f"- {plan['subject']} ({plan['expected_time']}시간 예상)")
            with col2:
                if st.button("✅ 완료", key=f"done_{i}"):
                    st.session_state.plans[i]["done"] = True

# -------------------------
# 2. 공부 기록
# -------------------------
with tab2:
    st.header("📖 공부 기록 입력")
    subject_log = st.selectbox("과목/주제 선택", [p["subject"] for p in st.session_state.plans if p["date"] == datetime.date.today()])
    real_time = st.number_input("실제 공부 시간(시간)", min_value=0.5, step=0.5)

    if st.button("공부 기록 저장"):
        st.session_state.logs.append({
            "date": datetime.date.today(),
            "subject": subject_log,
            "real_time": real_time
        })
        st.success(random.choice(messages))  # 응원 메시지 출력

    st.subheader("📌 오늘의 공부 기록")
    today_logs = [log for log in st.session_state.logs if log["date"] == datetime.date.today()]
    if today_logs:
        df = pd.DataFrame(today_logs)
        st.table(df)

# -------------------------
# 3. 주간 통계
# -------------------------
with tab3:
    st.header("📊 주간 통계")
    if st.session_state.logs:
        df = pd.DataFrame(st.session_state.logs)
        df["date"] = pd.to_datetime(df["date"])
        week_ago = datetime.date.today() - datetime.timedelta(days=7)
        weekly_df = df[df["date"].dt.date >= week_ago]

        if not weekly_df.empty:
            total_time = weekly_df["real_time"].sum()
            st.metric("이번 주 총 공부 시간", f"{total_time:.1f} 시간")

            chart = weekly_df.groupby("subject")["real_time"].sum().reset_index()
            st.bar_chart(chart.set_index("subject"))
        else:
            st.info("이번 주 공부 기록이 없습니다.")
    else:
        st.info("아직 기록이 없습니다.")
