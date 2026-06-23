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

pygame.init()

# Configurações da janela
LARGURA = 1280
ALTURA = 720

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Aprova ou Reprova")
fundo = pygame.image.load("imagens/fundo_tela_inicial.png")
fundo = pygame.transform.scale(fundo, (1280, 720))

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 120, 255)
AMARELO = (255, 215, 0)

# Fonte
fonte_titulo = pygame.font.Font("fontes\Starborn.ttf", 48)
fonte_botao = pygame.font.Font("fontes\Starborn.ttf", 40)
fonte_nome = pygame.font.SysFont(None, 35)
fonte_titulonome = pygame.font.SysFont(None, 40)

# Botão jogar
botao_jogar = pygame.Rect(535, 500, 230, 100)

# Campo de nome
input_box = pygame.Rect(450, 380, 400, 70)
nome_jogador = ""
ativo = False

rodando = True

while rodando:

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(evento.pos):
                ativo = True
            else:
                ativo = False

            if botao_jogar.collidepoint(evento.pos):
                print("Nome: ", nome_jogador)
                print("Jogo iniciado!")
        if evento.type == pygame.KEYDOWN and ativo:
            if evento.key == pygame.K_RETURN:
                print("Nome adicionado: ", nome_jogador)
            elif evento.key == pygame.K_BACKSPACE:
                nome_jogador = nome_jogador[:-1]
            else:
                nome_jogador += evento.unicode

    # Desenhar fundo
    tela.fill(BRANCO)
    fundo = pygame.image.load("imagens/fundo_tela_inicial.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    tela.blit(fundo,(0,0))

    # Desenhar título
    texto_titulo = fonte_titulo.render("Aprova ou Reprova", True, AMARELO)
    tela.blit(texto_titulo, (330, 180))

    # Desenhar botão
    pygame.draw.rect(tela, AMARELO, botao_jogar, border_radius=30)
    texto_botao = fonte_botao.render("Jogar", True, AZUL)

    # Centralizar texto do botão
    texto_rect = texto_botao.get_rect(center=botao_jogar.center)
    tela.blit(texto_botao, texto_rect)

    # Desenhar campo de nome
    pygame.draw.rect(tela, AMARELO, input_box, 7, border_radius=40)
    titulo_nome = fonte_titulonome.render("Digite seu nome", True, BRANCO)
    texto_nome = fonte_nome.render(nome_jogador or "Nome...", True, BRANCO)
    tela.blit(texto_nome, (input_box.x+60, input_box.y+25))
    tela.blit(titulo_nome, (540, 320))

    # Atualizar tela
    pygame.display.flip()

pygame.quit()
sys.exit()

nome = utils.nome_jogador()
jogador = Jogador(nome)

jogo.jogar(jogador, lista_disciplinas, perguntas_por_categoria, perguntas_tcc)

