import json
import os
from disciplina import Disciplina
from pergunta import Pergunta
from colorama import Fore, Style


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
        print(Fore.YELLOW + "👋 Bem-vindo ao Aprova ou Reprova!\n" + Style.RESET_ALL)
        nome = input("Qual o seu nome, Aluno?")
        if not nome:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Nome não pode ser vazio" + Style.RESET_ALL)
        elif len(nome)>20:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Nome muito longo" + Style.RESET_ALL)
        elif not nome.replace('_','').isalnum():
            print(Fore.LIGHTYELLOW_EX + "⚠️ Nome só deve conter letras, números e '_'" + Style.RESET_ALL)
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
        acertou = pergunta.verificar_resposta(resposta_do_usuario)
        if acertou == True:
            acertos += 1
    if acertos >= 3:
        return True
    else:
        return False

