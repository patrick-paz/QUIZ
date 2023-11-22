from fastapi import FastAPI

from . app import load_questao
# 
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/questoes")
def carregar_questao():
    return {"questões"}