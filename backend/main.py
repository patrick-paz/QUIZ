from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app import PerguntasLoader, Jogador, Quiz, PerguntasSelect, PergType

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Endpoint para iniciar o quiz
@app.post("/questoes")
def questões_quiz(tema: PergType, qtd_perg: int):

    data = 'data.json'
    questoes = PerguntasLoader.carregar_perguntas(data)
    perguntas = PerguntasSelect.load_questao(questoes, tema,qtd_perg)
    
    if not perguntas:
        raise HTTPException(status_code=404, detail="Nenhuma pergunta disponível para o tema selecionado.")
    

    return perguntas

# Endpoint para definir o jogador
@app.post("/jogador")
def definir_jogador(jogador_nome:str):
    # Crie uma instância da classe Jogador com o nome fornecido
    jogador = Jogador(nome=jogador_nome)
    
    return jogador

# @app.post("/inscrever")
# def inscrever_jogador(jogador: Jogador):
    # Crie uma instância da classe Jogador com o nome fornecido
    # quiz_inscrever = Quiz.inscrever(jogador)
    
    # Faça algo com o jogador, como armazená-lo em um banco de dados ou em uma variável global
    # ...
    
    # return quiz_inscrever
