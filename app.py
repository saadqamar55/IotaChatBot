import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

st.header("Iota Checker ChatBot")

def compute_iota_power(n: int) -> str:
    remainder = n % 4
    if remainder == 0:
        return "1"
    elif remainder == 1:
        return "i"
    elif remainder == 2:
        return "-1"
    elif remainder == 3:
        return "-i"

user_input = st.text_input("Enter the power of i:")

if st.button("Check"):
    #Check if input is a valid integer 
    if user_input.strip().lstrip("-+").isdigit():
        n = int(user_input)
        result = compute_iota_power(n)
        st.write(f"i^{n} = {result}")
    else:
        st.write("❌ Please enter a valid integer for the power of i.")
