import json
from disciplina import Disciplina
from pergunta import Pergunta


with open('disciplina.json', 'r', encoding = 'utf-8') as arq:
    lista_disciplinas = []
    
    for dados in json.load(arq):
        disciplina = Disciplina(
            dados['nome'],
            dados['periodo'],
            dados['categoria']
        )
        lista_disciplinas.append(disciplina)
with open('pergunta.json', 'r', encoding = 'utf-8') as arq:
    lista_perguntas = []
    
    for dados in json.load(arq):
        pergunta = Pergunta(
            dados['enunciado'],
            dados['categoria'],
            dados['alternativas'],
            dados['resposta']
        )
        lista_perguntas.append(pergunta)

nome = input("Qual seu nome, Aluno(a)?")
input(f"Olá! {nome}, você está iniciando no curso de BSI!\n Enter para continuar")

for periodo in range(1,10):
    disciplina_do_periodo = []
    print(f"Disciplinas do {periodo}:\n")
    for disciplina in lista_disciplinas:
        if disciplina.periodo == periodo:
            disciplina_do_periodo.append(disciplina)
            print(disciplina.nome)
    
