# chat.py

import streamlit as st
from  gpt import professor_virtual
from dotenv import load_dotenv
import openai
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Define a chave de API da OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

st.set_page_config(layout="centered")  # Centraliza o layout da página
st.image("logo.png", width=200)
st.title("Chat com Professor de Inglês Virtual")
   
user_input = st.text_input("Você:", "")
    
if user_input:
    prompt = f"Aluno: {user_input}\nProfessor de inglês:"
    response = professor_virtual(prompt)
    st.text_area("Professor:", value=response, height=200)
    st.write("Digite sua pergunta ou frase em inglês e pressione Enter para obter uma resposta do professor de inglês virtual.")
