import streamlit as st
import random

fortunes = ["恋実る", "恋少し実る", "恋ちょっと厳しそう", "恋諦めたほうがいいかも", "次の相手に行こうね"]

st.title("恋御籤")
st.write("下のボタンをクリックして、あなたの恋御籤を引いてください。")

if st.button("恋御籤を引く"):
    fortune = random.choice(fortunes)
    st.write(f"あなたの恋御籤は「{fortune}」です。")