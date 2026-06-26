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
                pygame.quit()
                sys.exit()
        
        tela.fill(constantes.BRANCO)
        desenhar_grade(tela, grade)

        texto = fonte_texto.render(f"{len(palavras_encontradas)} / {len(palavras)} encontradas", True, constantes.PRETO)
        tela.blit(texto, (50, 50))

        pygame.display.flip()

        if len(palavras_encontradas) == len(palavras):
            return "tela_pergunta"

def gerar_grade(periodo):

def desenhar_grade(tela, grade):