import pygame
import sys
from interface import constantes
import random

caca_palavras = {
    1: ["determinacao", "logica", "estudo", "jogo"],
    2: ["programar", "papel", "avaliacao", "departamento"],
    3: ["ler", "python", "sustentavel", "escrita", "professor"],
    4: ["nota", "boletim", "principal", "material", "universidade"],
    5: ["vaga", "conjunto", "aluno", "bolsa", "funcao"],
    6: ["gestao", "computador", "aprova", "amizade", "ferias"],
    7: ["reprova", "comunidade", "opcao", "curso", "sistema", "computacao"],
    8: ["aula", "administracao", "prova", "assunto", "questao", "cota"]
}

def minigame(tela, jogador, periodo):

    fundo = pygame.image.load("imagens/fundo_jogo.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    fonte_texto = pygame.font.SysFont("arial black", 40, bold=True)
                                   
    palavras = caca_palavras[periodo]
    grade = gerar_grade(periodo)
    palavras_encontradas = []

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 'tela_escolha'
        
        tela.fill(constantes.BRANCO)
        desenhar_grade(tela, grade, fonte_texto)

        texto = fonte_texto.render(f"{len(palavras_encontradas)} / {len(palavras)} encontradas", True, constantes.PRETO)
        tela.blit(texto, (50, 50))

        pygame.display.flip()

        if len(palavras_encontradas) == len(palavras):
            return 'tela_pergunta'

def gerar_grade(periodo, tamanho=15):

    palavras = caca_palavras[periodo]
    grade = [["" for _ in range(tamanho)] for _ in range(tamanho)]

    for palavra in palavras:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho-len(palavra))
        for i, letra in enumerate(palavra.upper()):
            grade[linha][coluna + i] = letra
    
    for i in range(tamanho):
        for j in range(tamanho):
            if grade[i][j] == "":
                grade[i][j] = chr(random.randint(65, 90))
    
    return grade

def desenhar_grade(tela, grade, fonte_texto):
    largura_celula = 60
    altura_celula = 40

    largura_grade = len(grade[0]) * largura_celula
    altura_grade = len(grade) * altura_celula

    # Ajuste horizontal e vertical
    offset_x = (constantes.LARGURA - largura_grade) // 2
    offset_y = 120

    for i, linha in enumerate(grade):
        for j, letra in enumerate(linha):
            rect = pygame.Rect(offset_x + j*largura_celula, offset_y + i*altura_celula, largura_celula, altura_celula)
            pygame.draw.rect(tela, constantes.AMARELO, rect, 2)
            texto = fonte_texto.render(letra, True, constantes.PRETO)
            tela.blit(texto, texto.get_rect(center=rect.center))