from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app import PerguntasLoader, Jogador, Quiz, PerguntasSelect, PergType

app = FastAPI()

# Modelo Pydantic para receber dados do jogador
class JogadorData(BaseModel):
    nome: str

# Endpoint para carregar perguntas
@app.get("/questoes")
def carregar_questao():
    data = 'data.json'
    questoes = PerguntasLoader.carregar_perguntas(data)
    return questoes

# Endpoint para iniciar o quiz
@app.post("/quiz")
def iniciar_quiz(tema: PergType):
    # jogador = Jogador(nome=jogador_data.nome)
    data = PerguntasLoader.carregar_perguntas('data.json')
    perguntas = PerguntasSelect.load_questao(data, tema)
    
    if not perguntas:
        raise HTTPException(status_code=404, detail="Nenhuma pergunta disponível para o tema selecionado.")
    

    return perguntas

# Endpoint para definir o jogador
@app.post("/jogador")
def definir_jogador(jogador_data: JogadorData):
    # Crie uma instância da classe Jogador com o nome fornecido
    jogador = Jogador(nome=jogador_data.nome)
    
    # Faça algo com o jogador, como armazená-lo em um banco de dados ou em uma variável global
    # ...
    
    return {"mensagem": f"Jogador definido como: {jogador.nome}"}
