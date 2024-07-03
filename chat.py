import streamlit as st
from gpt import professor_virtual
import openai
import os
from dotenv import load_dotenv

# Defina sua chave de API da OpenAI
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configurar proxy
os.environ['HTTPS_PROXY'] = "http://proxy.almg.uucp:3128"
os.environ['HTTP_PROXY'] = "http://proxy.almg.uucp:3128"

st.set_page_config(layout="centered")  # Centraliza o layout da página
st.image("logo.png", width=200)
st.title("Chat com Professor de Inglês Virtual")
   
user_input = st.text_input("Você:", "")
    
if user_input:
    prompt = f"Aluno: {user_input}\nProfessor de inglês:"
    response = professor_virtual(prompt)
    st.text_area("Professor:", value=response, height=200)
    st.write("Digite sua pergunta ou frase em inglês e pressione Enter para obter uma resposta do professor de inglês virtual.")
