import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="해민이의 공부 관리 앱", page_icon="📚", layout="wide")

# --- CSS 꾸미기 ---
st.markdown(
    """
    <style>
    body {
        background-color: #fffafc; /* 파스텔 핑크 배경 */
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    h1, h2, h3 {
        text-align: center;
        color: #ff6f91;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 타이틀 영역 ---
st.markdown("<h1>📚 공부 도우미 ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>시험 대비 스케줄링 ⏰ + 학습 피드백 💡 + 집중도 분석 📊</p>", unsafe_allow_html=True)

# --- 파일 로드/저장 함수 ---
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

# --- 입력 영역 ---
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📝 오늘의 공부 기록 입력")

    exam_date = st.date_input("📅 시험 날짜를 선택하세요", datetime.date.today())
    today = datetime.date.today()

    subjects_input = st.text_area("✏️ 오늘 공부한 과목과 시간을 입력하세요 (예: 수학 2, 영어 1)").split(",")

    col1, col2 = st.columns(2)
    with col1:
        focus = st.slider("🤓 집중도 (1~5)", 1, 5, 3)
    with col2:
        fatigue = st.slider("😵 피로도 (1~5)", 1, 5, 3)

    if st.button("💾 오늘 기록 저장하기"):
        rows = []
        for s in subjects_input:
            parts = s.strip().split()
            if len(parts) == 2:
                subj, hour = parts
                rows.append({"날짜": today, "과목": subj, "시간": float(hour), 
                             "집중도": focus, "피로도": fatigue})
        if rows:
            save_data(pd.DataFrame(rows))
            st.success("🎉 오늘의 기록이 저장되었습니다! 대단해요 👏👏")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 추천 기능 ---
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔮 AI 추천 기능")

    days_left = (exam_date - today).days
    st.write(f"⏰ 시험까지 **{days_left}일** 남았습니다!")

    importance_input = st.text_area("📊 과목 중요도 입력 (예: 수학 40, 영어 30)").split(",")

    if importance_input and days_left > 0:
        subj_split = [s.strip().split() for s in importance_input]
        subj_df = pd.DataFrame(subj_split, columns=["과목", "비중(%)"])
        subj_df["비중(%)"] = subj_df["비중(%)"].astype(float)
        subj_df["추천 시간(시간/일)"] = subj_df["비중(%)"] / 100 * 5
        st.markdown("### 📖 내일 추천 공부 시간표")
        st.table(subj_df)

    if subjects_input:
        st.subheader("💡 학습 피드백")
        st.write("✅ 오늘 공부 분석 결과:")
        for s in subjects_input:
            st.write(f"📌 {s.strip()}")
        st.write("🌱 내일은 부족했던 과목을 조금 더 보강해보세요!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 데이터 분석 ---
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 학습 데이터 분석")

    df = load_data()
    if not df.empty:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 집중도 & 피로도 추세")
            fig, ax = plt.subplots()
            grouped = df.groupby("날짜").mean(numeric_only=True)
            ax.plot(grouped.index, grouped["집중도"], marker="o", label="집중도 😊", color="hotpink")
            ax.plot(grouped.index, grouped["피로도"], marker="o", label="피로도 😴", color="skyblue")
            ax.set_ylabel("점수 (1~5)")
            ax.legend()
            st.pyplot(fig)

        with col2:
            st.subheader("📚 과목별 누적 공부 시간")
            subj_group = df.groupby("과목")["시간"].sum()
            fig2, ax2 = plt.subplots()
            subj_group.plot(kind="bar", ax=ax2, color="plum")
            ax2.set_ylabel("총 공부 시간(시간)")
            st.pyplot(fig2)

    else:
        st.info("📌 아직 저장된 공부 기록이 없어요! 오늘의 공부 기록을 먼저 입력해 주세요 📝")
    st.markdown("</div>", unsafe_allow_html=True)
