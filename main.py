import streamlit as st
import random

st.set_page_config(page_title="고전 타로 AI 리딩", page_icon="🃏", layout="centered")
st.markdown(
    """
    <div style="text-align:center; background-color:#f3e6d6; padding:15px; border-radius:10px;">
        <h1 style="color:#5b3a29;">🔮 고전 타로 3장 리딩 🔮</h1>
        <p style="font-size:18px;">카드를 뽑아 오늘의 운세를 확인해보세요!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 고전 타로 카드 데이터
cards = [
    {"name":"The Fool", "img":"https://upload.wikimedia.org/wikipedia/commons/5/53/RWS_Tarot_00_Fool.jpg"},
    {"name":"The Magician", "img":"https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg"},
    {"name":"The High Priestess", "img":"https://upload.wikimedia.org/wikipedia/commons/8/88/RWS_Tarot_02_High_Priestess.jpg"},
    {"name":"The Empress", "img":"https://upload.wikimedia.org/wikipedia/commons/d/d2/RWS_Tarot_03_Empress.jpg"},
    {"name":"The Emperor", "img":"https://upload.wikimedia.org/wikipedia/commons/0/01/RWS_Tarot_04_Emperor.jpg"},
    {"name":"The Lovers", "img":"https://upload.wikimedia.org/wikipedia/commons/7/7b/RWS_Tarot_06_Lovers.jpg"},
    {"name":"The Chariot", "img":"https://upload.wikimedia.org/wikipedia/commons/3/3a/RWS_Tarot_07_Chariot.jpg"},
    {"name":"The Sun", "img":"https://upload.wikimedia.org/wikipedia/commons/1/17/RWS_Tarot_19_Sun.jpg"},
    {"name":"The Moon", "img":"https://upload.wikimedia.org/wikipedia/commons/7/7a/RWS_Tarot_18_Moon.jpg"},
    {"name":"The Star", "img":"https://upload.wikimedia.org/wikipedia/commons/d/db/RWS_Tarot_17_Star.jpg"}
]

# 카드 뽑기
num_cards = 3
if st.button("✨ 3장 카드 뽑기 ✨"):
    chosen = random.sample(cards, num_cards)
    
    st.subheader("🎴 선택된 카드와 개별 해석")
    
    interpretations = []  # 각 카드 해석 저장
    for c in chosen:
        st.image(c["img"], width=150)
        st.markdown(f"<h3 style='color:#5b3a29;'>{c['name']}</h3>", unsafe_allow_html=True)
        
        # AI 해석 예시 (실제 OpenAI API 사용 가능)
        # prompt = f"{c['name']} 카드에 대한 오늘의 운세와 조언을 고전 타로 느낌으로 작성해줘."
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=[{"role":"system","content":"You are a classical tarot reader."},
        #               {"role":"user","content":prompt}]
        # )
        # interpretation = response['choices'][0]['message']['content']

        # 임시 해석 (랜덤 문구)
        example_texts = [
           "오늘 새로운 시작에 용기를 내보세요! 🌟",
    "직관을 믿고 작은 결정을 해보세요. ✨",
    "주변 사람들과의 관계에 신경 쓰면 좋은 날입니다. 💖",
    "조금 느긋하게 상황을 지켜보는 것이 좋습니다. 🍀",
    "집중력 있는 행동이 행운을 가져올 수 있어요. 🌸",
    "오늘은 마음의 평화를 찾는 것이 중요합니다. 🌙",
    "예상치 못한 기회가 찾아올 수 있어요. 🔮",
    "조금은 모험을 해보는 것도 좋습니다. 🐾",
    "타인의 의견을 경청하면 새로운 깨달음을 얻을 수 있어요. 💡",
    "자신의 감정을 솔직하게 표현해보세요. ❤️",
    "소소한 일에도 감사하는 마음을 가져보세요. 🌼",
    "오늘은 과거를 돌아보며 배움을 얻는 날입니다. 📜",
    "무리하지 말고 천천히 한 걸음씩 나아가세요. 🐢",
    "자신의 능력을 믿고 도전하면 좋은 결과가 있습니다. 💪",
    "작은 변화가 큰 기쁨을 가져올 수 있어요. 🎉",
    "오늘은 창의력을 발휘하면 좋은 성과가 있어요. 🎨",
    "타인에게 친절을 베풀면 행운이 찾아올 수 있어요. 🤝",
    "하루를 긍정적인 마음으로 시작해보세요. 🌞",
    "오늘은 과감한 결정을 내려도 괜찮습니다. 🏹",
    "내면의 소리에 귀 기울이면 올바른 길을 찾을 수 있어요. 🧘"
        ]
        interpretation = random.choice(example_texts)
        interpretations.append(interpretation)
        
        st.markdown(f"<p style='color:#5b3a29;'>{interpretation}</p>", unsafe_allow_html=True)

    # 종합 해석
    st.subheader("🔮 3장 카드 종합 해석")
    combined_interpretation = "오늘의 카드 3장을 종합하면:\n"
    combined_interpretation += " ".join(interpretations)
    combined_interpretation += "\n오늘은 직관과 용기를 믿고 행동하면 좋은 결과가 예상됩니다! 🌟"

    st.markdown(f"<p style='color:#5b3a29;'>{combined_interpretation}</p>", unsafe_allow_html=True)
    st.success("🐰 오늘의 고전 타로 3장 리딩이 완료되었습니다! 🃏✨")
