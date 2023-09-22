import streamlit as st
import random

fortunes = ["恋実る", "恋少し実る", "恋ちょっと厳しそう", "恋諦めたほうがいいかも", "次の相手に行こうね"]

st.title("恋みくじ")
st.write("下のボタンをクリックして、あなたの大事な恋を占おう！")

if st.button("恋みくじを引く"):
    fortune = random.choice(fortunes)
    st.write(f"あなたの恋みくじは「{fortune}」です。")