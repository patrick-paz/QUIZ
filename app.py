import json
from enum import Enum
import random

class Jogador:
    def __init__(self, nome, acertos=0):
        self.nome = nome
        self.acertos = acertos

class Pergunta:
    def __init__(self, id, pergunta, respostas, tema, dificuldade, resposta_correta):
        self.id = id
        self.pergunta = pergunta
        self.respostas = respostas
        self.tema = tema
        self.dificuldade = dificuldade
        self.resposta_correta = resposta_correta
        

class TemaStrategy:
    def selecionar(tema):
        pass

class SelecaoPorTema(TemaStrategy):
    def selecionar(perguntas, tema):
        return [pergunta for pergunta in perguntas if pergunta.tema == tema]

class SelecaoAleatoria(TemaStrategy):
    def selecionar(perguntas):
        numero_de_perguntas = 10 
        return random.sample([pergunta for pergunta in perguntas], numero_de_perguntas)

class PergType(Enum):
    
    CAPITAIS = "capitais"
    BIOLOGIA = "biologia"
    QUIMICA = "quimica"
    ASTRONOMIA = "astronomia"
    GEOGRAFIA = "geografia"
    ALEATORIO = "aleatorio"
        
class PerguntasFactory:

    def criar(data, tema: PergType):
        perguntas = []
        perguntas_select = []
        for pergunta_data in data:
            respostas = []
            resposta_correta = None
            for resposta in pergunta_data['resposta']:
                opcao = resposta['opcao']
                resCorreta = resposta['resCorreta']
                respostas.append(opcao)
                if resCorreta:
                    resposta_correta = opcao
            pergunta = Pergunta(
                pergunta_data['id'],
                pergunta_data['pergunta'],
                respostas,
                pergunta_data['tema'],
                pergunta_data['dificuldade'],
                resposta_correta
            )
            perguntas.append(pergunta)
            
        if tema != PergType.ALEATORIO:
            perguntas_select = SelecaoPorTema.selecionar(perguntas,tema.value)
        elif tema == PergType.ALEATORIO:
            perguntas_select = SelecaoAleatoria.selecionar(perguntas)
        
        return perguntas_select

class PerguntasLoader:
    @staticmethod
    def carregar_perguntas(data):
        with open(data, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
        
if __name__ == "__main__":
    
    jogador = Jogador(input("Insira seu nome: "))
    data = PerguntasLoader.carregar_perguntas('data.json')
    tema_escolhas = {
        "capitais": PergType.CAPITAIS,
        "biologia": PergType.BIOLOGIA,
        "quimica": PergType.QUIMICA,
        "astronomia": PergType.ASTRONOMIA,
        "geografia": PergType.GEOGRAFIA,
        "aleatorio": PergType.ALEATORIO
    }
    
    tema_enum = None
    while tema_enum is None:
        tema = input("Escolha um tema (capitais, biologia, quimica, astronomia, geografia, aleatorio): ").lower()
        tema_enum = tema_escolhas.get(tema)
        
        if tema_enum is not None:
            print(f"Jogador {jogador.nome}, você escolheu o tema: {tema_enum.value}")
        else:
            print("Tema inválido. Por favor, escolha um tema válido.")
    
    
    perguntas = []
    perguntas = PerguntasFactory.criar(data, tema_enum)
    for pergunta in perguntas:
        print("Pergunta:", pergunta.pergunta)
        print("Opções de Resposta:")
        for resposta in pergunta.respostas:
            print(resposta)
        print("Resposta Correta:", pergunta.resposta_correta)
