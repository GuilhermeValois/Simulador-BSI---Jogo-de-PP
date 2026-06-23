import pygame
import sys
from interface import constantes
from sistema import utils
pygame.init()

fonte_titulo = pygame.font.SysFont(None, constantes.TAMANHO_TITULO)
fonte_botao = pygame.font.SysFont(None, constantes.TAMANHO_TEXTO)

botao_jogar = pygame.Rect(490, 300, 300, 80)
botao_sair = pygame.Rect(490, 420, 300, 80)
fundo = pygame.image.load("imagens_jogo/fundo.png")
fundo = pygame.transform.scale(fundo,(constantes.LARGURA, constantes.ALTURA))

def mostra_menu(tela):

    pygame.display.set_caption("Aprova ou Reprova - Menu Inicial")

    rodando = True

    while rodando:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if botao_jogar.collidepoint(evento.pos):
                    estado = "tela_nome"
                    return estado
                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        # Fundo
        tela.fill(constantes.BRANCO)
        tela.blit(fundo,(0,0))
        # Título
        texto_titulo = fonte_titulo.render(
            "APROVA OU REPROVA",
            True,
            constantes.PRETO
        )

        tela.blit(texto_titulo, (320, 120))

        # Botão jogar
        pygame.draw.rect(tela, constantes.AMARELO, botao_jogar)

        texto_jogar = fonte_botao.render(
            "JOGAR",
            True,
            constantes.PRETO
        )

        tela.blit(texto_jogar, (580, 325))

        # Botão sair
        pygame.draw.rect(tela, constantes.AMARELO, botao_sair)

        texto_sair = fonte_botao.render(
            "SAIR",
            True,
            constantes.PRETO
        )

        tela.blit(texto_sair, (605, 445))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def tela_inicial(tela):
    pygame.init()

    # Configurações da janela

    pygame.display.set_caption("Aprova ou Reprova")
    fundo = pygame.image.load("imagens/fundo_tela_inicial.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))

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
    invalidez = ''
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
                    if utils.valida_nome(nome_jogador):
                        estado = 'tela_pergunta'
                        return nome_jogador, estado
                    else:
                        invalidez = 'Nome Inválido'
            if evento.type == pygame.KEYDOWN and ativo:
                if evento.key == pygame.K_RETURN:
                    print("Nome adicionado: ", nome_jogador)
                    if utils.valida_nome(nome_jogador):
                        estado = 'tela_pergunta'
                        return nome_jogador, estado
                elif evento.key == pygame.K_BACKSPACE:
                    invalidez = ''
                    nome_jogador = nome_jogador[:-1]
                else:
                    invalidez = ''
                    nome_jogador += evento.unicode

        # Desenhar fundo
        tela.fill(constantes.BRANCO)
        fundo = pygame.image.load("imagens/fundo_tela_inicial.png")
        fundo = pygame.transform.scale(fundo, (1280, 720))
        tela.blit(fundo,(0,0))

        # Desenhar título
        texto_titulo = fonte_titulo.render("Aprova ou Reprova", True, constantes.AMARELO)
        tela.blit(texto_titulo, (330, 180))

        # Desenhar botão
        pygame.draw.rect(tela, constantes.AMARELO, botao_jogar, border_radius=30)
        texto_botao = fonte_botao.render("Jogar", True, constantes.AZUL)

        # Centralizar texto do botão
        texto_rect = texto_botao.get_rect(center=botao_jogar.center)
        tela.blit(texto_botao, texto_rect)

        # Desenhar campo de nome
        if invalidez:
            texto_exibido = invalidez
            nome_jogador = ''
        elif nome_jogador:
            texto_exibido = nome_jogador
        else:
            texto_exibido = "Nome..."
        pygame.draw.rect(tela, constantes.AMARELO, input_box, 7, border_radius=40)
        titulo_nome = fonte_titulonome.render("Digite seu nome", True, constantes.BRANCO)
        texto_nome = fonte_nome.render(texto_exibido, True, constantes.BRANCO)
        tela.blit(texto_nome, (input_box.x+60, input_box.y+25))
        tela.blit(titulo_nome, (540, 320))

        # Atualizar tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()