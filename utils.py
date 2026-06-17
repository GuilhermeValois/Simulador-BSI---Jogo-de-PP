import json
import os
from disciplina import Disciplina
from pergunta import Pergunta
import colorama


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
def carregar_tcc():

    ARQUIVO_PERGUNTAS = os.path.join(os.path.dirname(__file__),'data', 'tcc.json')

    with open(ARQUIVO_PERGUNTAS, 'r', encoding = 'utf-8') as arq:
        perguntas_tcc = []
    
        for dados in json.load(arq):
            pergunta = Pergunta(
                dados['enunciado'],
                dados['categoria'],
                dados['alternativas'],
                dados['resposta']
            )
            perguntas_tcc.append(pergunta)
    return perguntas_tcc

def nome_jogador():
    while True:
        print("Bem-vindo ao Aprova ou Reprova!\n")
        nome = input("Qual o seu nome, Aluno?")
        if not nome:
            print("Nome não pode ser vazio")
        elif len(nome)>20:
            print("Nome muito longo")
        elif not nome.replace('_','').isalnum():
            print("Nome só deve conter letras, números e '_'")
        else:
            return nome
        
def disciplina_por_periodo(lista_de_disciplinas, periodo):
    disciplinas_do_periodo = []
    for disciplina in lista_de_disciplinas:
        if disciplina.periodo == periodo:
            disciplinas_do_periodo.append(disciplina)
    print("Disciplinas:")
    for disciplina in disciplinas_do_periodo:
        print(f"{disciplina.nome}\n")
    return disciplinas_do_periodo

def fazer_tcc(perguntas_tcc):    
    acertos = 0
    for pergunta in perguntas_tcc:
        pergunta.mostrar_pergunta()
        resposta_do_usuario = input("").strip().upper()
        acertou = pergunta.verificar_resposta(resposta_do_usuario, disciplina, jogador)
        if acertou == True:
            acertos += 1
    if acertos >= 3:
        return True
    else:
        return False

