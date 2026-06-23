import pygame
import sys
from interface import constantes

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

