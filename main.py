import streamlit as st

# 추천할 직업 리스트
jobs = [
    "소프트웨어 엔지니어",
    "디자이너",
    "마케팅 전문가",
    "데이터 분석가",
    "선생님",
    "의사",
    "작가",
    "요리사",
    "게임 개발자",
    "심리상담사"
]

st.title("이름으로 어울리는 직업 추천")
st.write("이름을 입력하면 어울리는 직업을 추천해드립니다!")

name = st.text_input("이름을 입력하세요:")

if name:
    # 이름의 유니코드 값 합으로 직업 인덱스 계산
    index = sum(ord(c) for c in name) % len(jobs)
    recommended_job = jobs[index]
    
    st.write(f"**{name}님께 어울리는 직업은:** {recommended_job} 입니다!")
