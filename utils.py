import json
import os
from disciplina import Disciplina
from pergunta import Pergunta


def carregar_disciplinas():

    ARQUIVO_DISCIPLINAS = os.path.join(os.path.dirname(__file__),'data', 'disciplina.json')
    
    with open(ARQUIVO_DISCIPLINAS, 'r', encoding = 'utf-8') as arq:
        lista_disciplinas = []
    
        for dados in json.load(arq):
            disciplina = Disciplina(
                dados['nome'],
                dados['periodo'],
                dados['categoria']
            )
            lista_disciplinas.append(disciplina)
    return lista_disciplinas

def carregar_perguntas():

    ARQUIVO_PERGUNTAS = os.path.join(os.path.dirname(__file__),'data', 'pergunta.json')

    with open(ARQUIVO_PERGUNTAS, 'r', encoding = 'utf-8') as arq:
        lista_perguntas = []
    
        for dados in json.load(arq):
            pergunta = Pergunta(
                dados['enunciado'],
                dados['categoria'],
                dados['alternativas'],
                dados['resposta']
            )
            lista_perguntas.append(pergunta)
    return lista_perguntas
