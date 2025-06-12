import streamlit as st
import random


title_emoji = "🎉🪨📄✂️ 가위바위보 게임 🖐️🔥"
choices = {
    "가위✌️": "✌️",
    "바위✊": "✊",
    "보🖐": "🖐"
}
results_emoji = {
    "win": "🎊🎉 승리! 🎉🎊",
    "lose": "😢 패배... 😢",
    "draw": "🤝 무승부 🤝"
}


st.set_page_config(page_title="화려한 가위바위보 게임", page_icon="✂️")
st.markdown(f"<h1 style='text-align:center; color:#ff4b4b;'>{title_emoji}</h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("""
<div style="background: linear-gradient(45deg, #ff9a9e, #fad0c4);
            padding: 20px; border-radius: 15px; text-align:center;">
    <h3 style="color:#fff;">아래에서 선택하세요! 👇</h3>
</div>
""", unsafe_allow_html=True)


user_choice = st.radio(
    "당신의 선택:",
    options=list(choices.keys()),
    index=0,
    horizontal=True
)

if st.button("결과 보기!"):
   
    comp_choice = random.choice(list(choices.keys()))

  
    def judge(user, comp):
        if user == comp:
            return "draw"
        elif (user == "가위✌️" and comp == "보🖐") or \
             (user == "바위✊" and comp == "가위✌️") or \
             (user == "보🖐" and comp == "바위✊"):
            return "win"
        else:
            return "lose"

    result = judge(user_choice, comp_choice)


    st.markdown("---")
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #f6d365, #fda085);
                border-radius: 20px; padding: 30px; text-align:center; color:#fff; font-size:22px;">
        <p>👤 당신의 선택: <b>{user_choice}</b></p>
        <p>🤖 컴퓨터의 선택: <b>{comp_choice}</b></p>
        <h2 style="margin-top:20px;">{results_emoji[result]}</h2>
    </div>
    """, unsafe_allow_html=True)

    
    if result == "win":
        st.balloons()
    elif result == "lose":
        st.snow()


st.markdown("""
<br><br>
<footer style="text-align:center; font-size:14px; color:#aaa;">
    Made with ❤️ by ChatGPT | 즐겁게 가위바위보 하세요! ✂️🖐️✊
</footer>
""", unsafe_allow_html=True)
