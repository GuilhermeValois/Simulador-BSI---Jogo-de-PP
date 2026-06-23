import json
import os
from classes.disciplina import Disciplina
from classes.pergunta import Pergunta
from colorama import Fore, Style
import pygame
import sys
from interface import constantes
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime

def limpar():
    os.system('cls')

def carregar_disciplinas():

    ARQUIVO_DISCIPLINAS = os.path.join(os.path.dirname(__file__),'..','data', 'disciplina.json')
    
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

    ARQUIVO_PERGUNTAS = os.path.join(os.path.dirname(__file__),'..','data', 'pergunta.json')

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

    ARQUIVO_PERGUNTAS = os.path.join(os.path.dirname(__file__),'..','data', 'tcc.json')

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

def valida_nome(nome):

    #while True:
        #limpar()
        #print(Fore.YELLOW + "👋 BEM-VINDO AO APROVA OU REPROVA!\n" + Style.RESET_ALL)
        #nome = input(Fore.LIGHTYELLOW_EX + "🤔 Qual o seu nome, Aluno? " + Style.RESET_ALL)
        if not nome:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Nome não pode ser vazio" + Style.RESET_ALL)
            return False
        elif len(nome)>20:
            print(Fore.LIGHTYELLOW_EX + "⚠️ Nome muito longo" + Style.RESET_ALL)
            return False
        elif not nome.replace('_','').isalnum():
            print(Fore.LIGHTYELLOW_EX + "⚠️ Nome só deve conter letras, números e '_'" + Style.RESET_ALL)
            return False
        else:
            return True
    
def disciplina_por_periodo(lista_de_disciplinas, periodo, nome):
    disciplinas_do_periodo = []
    for disciplina in lista_de_disciplinas:
        if disciplina.periodo == periodo:
            disciplinas_do_periodo.append(disciplina)
    limpar()
    print("="*50)
    print(Fore.LIGHTYELLOW_EX + "👤 Aluno(a): " + Style.RESET_ALL + Fore.GREEN + f"{nome}" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + f"📚 Disciplinas do {periodo}º período:" + Style.RESET_ALL)
    for disciplina in disciplinas_do_periodo:
        print(Fore.CYAN + f"- {disciplina.nome}" + Style.RESET_ALL)
    print("="*50)
    print("")
    return disciplinas_do_periodo

def fazer_tcc(perguntas_tcc):    
    acertos = 0
    for pergunta in perguntas_tcc:
        pergunta.mostrar_pergunta()
        resposta_do_usuario = input(Fore.LIGHTYELLOW_EX + "📝 Sua resposta: " + Style.RESET_ALL).strip().upper()
        acertou = pergunta.verificar_resposta(resposta_do_usuario)
        if acertou == True:
            acertos += 1
    if acertos >= 3:
        return True
    else:
        return False

def quebrar_texto(texto, fonte, largura_maxima):
    
    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:

        teste = linha_atual + palavra + " "

        if fonte.size(teste)[0] <= largura_maxima:
            linha_atual = teste
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "

    linhas.append(linha_atual)

    return linhas

def contador(tela, fonte, segundos,mensagem):

    inicio = pygame.time.get_ticks()

    while True:

        restante = segundos - (pygame.time.get_ticks() - inicio) // 1000

        if restante <= 0:
            break

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill(constantes.BRANCO)
        tela.blit(mensagem, (mensagem.get_rect(center=(1280//2,400))))

        texto = fonte.render(f"Próxima pergunta em {restante}",True,constantes.PRETO)

        tela.blit(texto,texto.get_rect(center=(640, 360)))

        pygame.display.flip()

def cronometro(tela, fonte, segundos):

    inicio = pygame.time.get_ticks()

    restante = segundos - (pygame.time.get_ticks() - inicio) // 1000

    if restante <= 0:
        tempo_acabou = True
        return True
    texto = fonte.render(
        f"Cronômetro: {restante}",
        True,
        constantes.PRETO
    )

    tela.blit(
        texto,
        texto.get_rect(center=(640, 360))
        )

def desenhar_borda(canvas, doc):
    largura, altura = doc.pagesize

    # Borda externa
    canvas.setStrokeColor(colors.darkblue)
    canvas.setLineWidth(4)
    canvas.rect(30, 30, largura - 60, altura - 60)

    # Borda interna
    canvas.setLineWidth(2)
    canvas.rect(45, 45, largura - 90, altura - 90)


def gerar_certificado(nome_aluno):

    arquivo = f"Certificado_{nome_aluno}.pdf"

    pdf = SimpleDocTemplate(arquivo)

    estilos = getSampleStyleSheet()

    estilo_titulo = ParagraphStyle(
        "Titulo",
        parent=estilos["Title"],
        alignment=TA_CENTER,
        textColor=colors.darkblue,
        fontSize=28,
    )

    estilo_nome = ParagraphStyle(
        "Nome",
        parent=estilos["Normal"],
        alignment=TA_CENTER,
        fontSize=22,
        textColor=colors.black,
    )

    estilo_texto = ParagraphStyle(
        "Texto",
        parent=estilos["Normal"],
        alignment=TA_CENTER,
        fontSize=14,
        leading=24,
    )

    elementos = []

    elementos.append(Spacer(1, 80))

    elementos.append(
        Paragraph(
            "CERTIFICADO DE CONCLUSÃO",
            estilo_titulo
        )
    )

    elementos.append(Spacer(1, 40))

    elementos.append(
        Paragraph(
            "Certificamos que",
            estilo_texto
        )
    )

    elementos.append(Spacer(1, 15))

    elementos.append(
        Paragraph(
            f"<b>{nome_aluno}</b>",
            estilo_nome
        )
    )

    elementos.append(Spacer(1, 25))

    elementos.append(
        Paragraph(
            "concluiu com sucesso o curso de "
            "<b>Bacharelado em Sistemas de Informação</b> "
            "no jogo educacional <b>Aprova ou Reprova</b>, "
            "demonstrando dedicação, esforço e conhecimento "
            "ao longo de sua trajetória acadêmica.",
            estilo_texto
        )
    )

    elementos.append(Spacer(1, 50))

    data = datetime.now().strftime("%d/%m/%Y")

    elementos.append(
        Paragraph(
            f"Recife, {data}",
            estilo_texto
        )
    )

    elementos.append(Spacer(1, 80))

    elementos.append(
        Paragraph(
            "______________________________",
            estilo_texto
        )
    )

    elementos.append(
        Paragraph(
            "Coordenação do Curso",
            estilo_texto
        )
    )

    pdf.build(
        elementos,
        onFirstPage=desenhar_borda
    )

    print(f"Certificado gerado: {arquivo}")