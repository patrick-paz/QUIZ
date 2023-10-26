import json
from enum import Enum
import random
from abc import ABC



class Subject(ABC): # Aquele que notifica os interessados
    """ Abstract subject """
    def inscrever(self, observer):
        pass
    def notificar(self):
        pass
class Observer(ABC):
    def atualizar(self):
        pass

class Jogador(Observer):
    def __init__(self, nome, acertos=0, subject=None):
        self.nome = nome
        self.acertos = acertos
        self.subject = subject
        if subject:
            
            subject.inscrever(self)
            
    def atualizar(self):
        self.acertos += 1
        print()
        print("#"*18)
        print(f"### ACERTOS: {self.acertos} ###")
        print("#"*18)
        print()
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
        
        
class Quiz(Subject):
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.indice_pergunta = 0
        self.inscritos = []

    def inscrever(self, observer):
        if observer not in self.inscritos:
            self.inscritos.append(observer)
            
    def notificar(self):
        for observer in self.inscritos:
            observer.atualizar()

    def iniciar(self):
        while self.indice_pergunta < len(self.perguntas):
            perguntas = self.perguntas[self.indice_pergunta]
            print("#" * 40)
            print(f"Tema: {perguntas.tema} -- Pergunta {self.indice_pergunta + 1}: {perguntas.pergunta}")
            for i, resposta in enumerate(perguntas.respostas):
                print(f"{i + 1}. {resposta}")
            resposta_jogador = int(input("Escolha sua resposta: ")) - 1  # Subtrai 1 para obter o índice correto na lista
            
            if perguntas.respostas[resposta_jogador] == perguntas.resposta_correta:
                print("Acertou!")
                self.notificar()
            else:
                print("Errou. A resposta correta era:", perguntas.resposta_correta)
            
            self.indice_pergunta += 1
            

        
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
    print()
    tema_enum = None
    while tema_enum is None:
        tema = input("Escolha um tema (capitais, biologia, quimica, astronomia, geografia, aleatorio): ").lower()
        tema_enum = tema_escolhas.get(tema)
        
        if tema_enum is not None:
            print()
            print(f"Jogador {jogador.nome}, você escolheu o tema: {tema_enum.value}")
        else:
            print()
            print("Tema inválido. Por favor, escolha um tema válido.")
    
    print()
    perguntas = []
    perguntas = PerguntasFactory.criar(data, tema_enum)
    
    quiz = Quiz(perguntas)
    quiz.inscrever(jogador)
    
    quiz.iniciar()
    
    total_perg = len(perguntas)
    print("="*40)
    print(f"======== TOTAL DE ACERTOS: {jogador.acertos} / {total_perg} =======")
    print("="*40)
