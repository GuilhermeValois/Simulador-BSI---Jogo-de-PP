import math
import pygame
import sys
from interface import constantes
from sistema import utils


def tela_inicial(tela):
    pygame.init()

    # Configurações da janela

    pygame.display.set_caption("Aprova ou Reprova")
    fundo = pygame.image.load("imagens/fundo_tela_inicial.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))

    # Fonte
    fonte_titulo = pygame.font.Font("fontes\Starborn.ttf", 60)
    fonte_nome = pygame.font.SysFont("Segoe UI Emoji", 25)
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
        texto_titulo_sombra = fonte_titulo.render("Aprova ou Reprova", True, constantes.CINZA_ESCURO)
        texto_titulo = fonte_titulo.render("Aprova ou Reprova", True, constantes.AMARELO)
        
        # Posição titulo
        pos_x, pos_y = 250, 180

        tela.blit(texto_titulo_sombra, (pos_x+3, pos_y+3))
        tela.blit(texto_titulo, (pos_x, pos_y))

        # Desenhar campo de nome
        if invalidez:
            texto_exibido = invalidez
            nome_jogador = ''
        elif nome_jogador:
            texto_exibido = "👤 " + nome_jogador
        else:
            texto_exibido = "👤 Nome..."
        pygame.draw.rect(tela, constantes.CINZA_CLARO, input_box, border_radius=40)
        pygame.draw.rect(tela, constantes.BRANCO, input_box, 7, border_radius=40)
        titulo_nome = fonte_titulonome.render("Digite seu nome", True, constantes.BRANCO)
        texto_nome = fonte_nome.render(texto_exibido, True, constantes.PRETO)
        tela.blit(texto_nome, (input_box.x+40, input_box.y+25))
        tela.blit(titulo_nome, (540, 320))

        # Botão pulsante
        tempo = pygame.time.get_ticks()/500
        pulsar = 8*math.sin(tempo)

        rect_animado = pygame.Rect(
            botao_jogar.x - pulsar/2,
            botao_jogar.y - pulsar/2,
            botao_jogar.width + pulsar,
            botao_jogar.height + pulsar
        )

        # Sombra do botão
        pygame.draw.rect(tela, constantes.AMARELO_ESCURO, rect_animado.move(5, 5), border_radius=30)

        # Desenhar botão
        pygame.draw.rect(tela, constantes.AMARELO, rect_animado, border_radius=30)

        # Texto pulsante
        fonte_botao = pygame.font.Font("fontes\Starborn.ttf", int(40 + pulsar/2))
        texto_botao = fonte_botao.render("Jogar", True, constantes.AZUL)

        # Sombra do texto
        texto_botao_sombra = fonte_botao.render("Jogar", True, constantes.CINZA_ESCURO)
        texto_rect = texto_botao.get_rect(center=rect_animado.center)
        tela.blit(texto_botao_sombra, (texto_rect.x+3, texto_rect.y+3))

        # Texto botão
        tela.blit(texto_botao, texto_rect)


        # Atualizar tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()