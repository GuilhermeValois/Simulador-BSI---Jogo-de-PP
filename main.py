import utils
from jogador import Jogador
import jogo
import pygame
import sys

lista_disciplinas = utils.carregar_disciplinas()
lista_perguntas = utils.carregar_perguntas()
perguntas_tcc = utils.carregar_tcc()

perguntas_por_categoria = {
    'programacao': [],
    'matematica_logica': [],
    'dados': [],
    'infraestrutura': [],
    'sistemas_informacao': [],
    'gestao': []
}

for pergunta in lista_perguntas:
    perguntas_por_categoria[pergunta.categoria].append(pergunta)

nome = utils.nome_jogador()
jogador = Jogador(nome)

jogo.jogar(jogador, lista_disciplinas, perguntas_por_categoria, perguntas_tcc)
pygame.init()

# Configurações da janela
LARGURA = 1280
ALTURA = 720

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulador BSI")
fundo = pygame.image.load("imagens/fundo_tela_inicial.png")
fundo = pygame.transform.scale(fundo, (1280, 720))

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 120, 255)
AMARELO = (255, 215, 0)

# Fonte
fonte_titulo = pygame.font.SysFont(None, 60)
fonte_botao = pygame.font.SysFont(None, 40)

# Botão jogar
botao_jogar = pygame.Rect(540, 300, 200, 80)

rodando = True

while rodando:

    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:

            if botao_jogar.collidepoint(evento.pos):
                print("Jogo iniciado!")

    # Desenhar fundo
    tela.fill(BRANCO)
    fundo = pygame.image.load("imagens/fundo_tela_inicial.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    tela.blit(fundo,(0,0))

    # Desenhar título
    texto_titulo = fonte_titulo.render(
        "SIMULADOR BSI",
        True,
        PRETO
    )

    tela.blit(texto_titulo, (470, 100))

    # Desenhar botão
    pygame.draw.rect(tela, AMARELO, botao_jogar)

    texto_botao = fonte_botao.render(
        "JOGAR",
        True,
        BRANCO
    )

    
    tela.blit(texto_botao, (595, 325))

    # Atualizar tela
    pygame.display.flip()

pygame.quit()
sys.exit()

