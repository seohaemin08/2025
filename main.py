import streamlit as st
import random

st.set_page_config(page_title="고전 타로 AI 리딩", page_icon="🃏", layout="centered")
st.markdown(
    """
    <div style="text-align:center; background-color:#f3e6d6; padding:15px; border-radius:10px;">
        <h1 style="color:#5b3a29;">🔮 고전 타로 카드 리딩 🔮</h1>
        <p style="font-size:18px;">카드를 뽑아 오늘의 운세와 조언을 확인해보세요!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 고전 타로 카드 데이터 (Rider-Waite 이미지)
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
num_cards = st.slider("몇 장의 카드를 뽑으시겠어요?", 1, 3, 3)
if st.button("✨ 카드 뽑기 ✨"):
    chosen = random.sample(cards, num_cards)

    st.subheader("🎴 선택된 카드 (고전 타로)")
    for c in chosen:
        st.image(c["img"], width=150)
        st.markdown(f"<h3 style='color:#5b3a29;'>{c['name']}</h3>", unsafe_allow_html=True)

    # AI 해석 (실제 OpenAI API 사용 가능)
    # prompt = f"다음 고전 타로 카드들에 대해 오늘의 운세와 조언을 해석해줘: {', '.join([c['name'] for c in chosen])}"
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "system", "content": "You are a classical tarot reader."},
    #               {"role": "user", "content": prompt}]
    # )
    # interpretation = response['choices'][0]['message']['content']

    # 임시 해석
    interpretation = """
    오늘은 새로운 시작에 용기를 내보세요. 🌟
    작은 결정이 큰 변화를 가져올 수 있습니다.
    내면의 직관을 믿고 행동하면 좋은 결과가 있을 거예요.
    """

    st.subheader("🔮 AI 카드 해석")
    st.markdown(f"<p style='color:#5b3a29;'>{interpretation}</p>", unsafe_allow_html=True)

    st.success("오늘의 고전 타로 리딩이 완료되었습니다! 🃏✨")
