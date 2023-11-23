from fastapi import FastAPI

from app import PerguntasLoader

# 
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/questoes")
def carregar_questao():
    data = 'data.json'
    questoes = PerguntasLoader.carregar_perguntas(data)
    return questoes