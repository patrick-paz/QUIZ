from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app import PerguntasLoader, PerguntasSelect, PergType, Quiz, Jogador, Pergunta

app = FastAPI()

class JogadorModel(BaseModel):
    
    nome: str

class RepostasModel(BaseModel):
    
    jogador_resposta: str
    resposta_correta: str


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
jogador_global = None

@app.post("/definir_jogador", response_model=JogadorModel)
def definir_jogador(jogador: JogadorModel):
    global jogador_global
    jogador_global = Jogador(nome=jogador.nome)
    return {"nome": jogador_global.nome}

@app.get("/get_jogador")
def get_jogador():
    global jogador_global
    if jogador_global is None:
        raise HTTPException(status_code=404, detail="Jogador não definido.")
    return {"nome": jogador_global.nome, "acertos": jogador_global.acertos}

@app.post("/atualizar_acerto")
def atualizar_acerto(dados: RepostasModel):
    global jogador_global
    
    jogador_resposta = dados.jogador_resposta
    resposta_correta = dados.resposta_correta
    
    aviso = Pergunta.corrigir(jogador_resposta, resposta_correta, jogador_global)
    
    return aviso
    


