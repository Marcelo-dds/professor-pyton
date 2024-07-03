# gpt_utils.py

import openai
import os

# Carrega variáveis de ambiente do arquivo .env
from dotenv import load_dotenv
load_dotenv()

# Define a chave de API da OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configurar proxy, se necessário
os.environ['HTTPS_PROXY'] = "http://proxy.almg.uucp:3128"
os.environ['HTTP_PROXY'] = "http://proxy.almg.uucp:3128"

# Função para interagir com GPT
def professor_virtual(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an English teacher."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Erro ao se comunicar com a API: {e}"
