import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="📚 공부 도우미 앱", layout="centered")

# --- 타이틀 ---
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>✨ 공부 도우미 앱 🐥🌸</h1>", unsafe_allow_html=True)
st.write("공부 계획을 세우고 귀엽게 관리해보세요! 🐰📖💖")

# --- CSV 파일 설정 ---
LOG_FILE = "study_log.csv"

def load_data():
    if os.path.exists(LOG_FILE):
        return pd.read_csv(LOG_FILE)
    else:
        return pd.DataFrame(columns=["날짜", "과목", "시간", "집중도", "피로도"])

def save_data(new_data):
    df = load_data()
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(LOG_FILE, index=False)

# --- 오늘 공부 기록 입력 ---
st.markdown("## 📝 오늘의 공부 기록 입력")
exam_date = st.date_input("📅 시험 날짜", datetime.date.today())
today = datetime.date.today()
subjects_input = st.text_area("✏️ 오늘 공부한 과목과 시간을 입력 (예: 수학 2, 영어 1)").split(",")

col1, col2, col3 = st.columns([1,1,1])
with col1:
    focus = st.slider("🤓 집중도 (1~5)", 1, 5, 3)
with col2:
    fatigue = st.slider("😵 피로도 (1~5)", 1, 5, 3)
with col3:
    goal_time = st.number_input("⏱ 오늘 목표 공부 시간(시간)", min_value=0, value=5)

if st.button("💾 오늘 기록 저장"):
    rows = []
    total_time = 0
    for s in subjects_input:
        parts = s.strip().split()
        if len(parts) == 2:
            subj, hour = parts
            try:
                hour_val = float(hour)
                total_time += hour_val
                rows.append({"날짜": today, "과목": subj, "시간": hour_val, 
                             "집중도": focus, "피로도": fatigue})
            except:
                st.warning(f"⚠️ '{s}' 형식이 올바르지 않습니다.")
    if rows:
        save_data(pd.DataFrame(rows))
        st.success("🎉 오늘 기록 저장 완료! 🐰")

        # ✅ 오늘 공부 달성률 표시
        percent = min(int((total_time/goal_time)*100),100)
        st.progress(percent)
        st.write(f"오늘 목표 달성률: {percent}% ⏱")

        # ✅ 랜덤 격려 메시지
        messages = ["오늘도 열공! 🐰💖", "작은 성취도 큰 발전! 🌸✨", "계속하면 꿈에 가까워져요! 🐥💡"]
        st.info(random.choice(messages))

# --- AI 추천 기능 ---
st.markdown("## 🔮 AI 추천 기능")
days_left = (exam_date - today).days
st.write(f"⏰ 시험까지 **{days_left}일** 남았습니다!")

importance_input = st.text_area("📊 과목 중요도 입력 (예: 수학:40, 영어:30, 과학:30)", "수학:40, 영어:30, 과학:30")

subj_split = []
if importance_input.strip():
    try:
        for item in importance_input.split(","):
            if ":" in item:
                subj, val = item.split(":")
                subj_split.append([subj.strip(), int(val.strip())])
        if subj_split:
            subj_df = pd.DataFrame(subj_split, columns=["과목", "비중(%)"])
            st.markdown("### 📖 추천 공부 시간표")
            st.dataframe(subj_df, use_container_width=True)

            # 원형 그래프
            st.markdown("### 🎨 과목 비중 그래프")
            fig, ax = plt.subplots()
            colors = ["#FFC0CB", "#FFB6C1", "#FF69B4", "#FF1493", "#FF82A9"]
            ax.pie(subj_df["비중(%)"], labels=subj_df["과목"], autopct="%1.1f%%", startangle=90, colors=colors)
            ax.axis("equal")
            st.pyplot(fig)
    except Exception as e:
        st.error("⚠️ 입력 형식 오류! 예: 수학:40, 영어:30, 과학:30")

# --- 학습 데이터 분석 ---
st.markdown("## 📈 학습 데이터 분석")
df = load_data()
if not df.empty:
    # 집중도/피로도 추세
    st.write("📊 집중도 & 피로도 추세")
    daily = df.groupby("날짜")[["집중도","피로도"]].mean().reset_index()
    st.line_chart(daily.set_index("날짜"))

    # 과목별 누적 공부 시간
    st.write("📚 과목별 누적 공부 시간")
    subj_group = df.groupby("과목")["시간"].sum().reset_index()
    st.bar_chart(subj_group.set_index("과목"))

    # 집중도 기반 과목 추천
    st.write("💡 집중도 기반 오늘의 추천")
    if len(df) >= 3:  # 최근 3일 이상 데이터 있을 때
        recent = df.tail(5)
        avg_focus = recent.groupby("과목")["집중도"].mean().sort_values()
        low_focus = avg_focus.head(2)
        high_focus = avg_focus.tail(2)
        st.write("📌 집중도 낮은 과목 (짧게 복습 추천):")
        for subj, val in low_focus.items():
            st.write(f"- {subj}: 평균 집중도 {val:.1f} 😴")
        st.write("📌 집중도 높은 과목 (심화 학습 추천):")
        for subj, val in high_focus.items():
            st.write(f"- {subj}: 평균 집중도 {val:.1f} 😊")

    # 과목별 평균 집중도 & 피로도
    st.write("📊 과목별 평균 집중도 & 피로도")
    subj_stats = df.groupby("과목")[["집중도","피로도"]].mean()
    st.dataframe(subj_stats.style.format("{:.1f}"))

else:
    st.info("📌 기록이 없습니다. 오늘부터 시작해 보세요! 🐥")
