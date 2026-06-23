import pygame
import sys
from interface import constantes
from sistema import utils

pygame.init()

fonte_titulo = pygame.font.SysFont(None,constantes.TAMANHO_TITULO)
fonte_botao = pygame.font.SysFont(None, constantes.TAMANHO_TEXTO)


botao_confirma_nome = pygame.Rect(490, 300, 300, 80)
botao_voltar = pygame.Rect(490, 420, 300, 80)
espaco_nome = pygame.Rect(465, 200, 350, 50)

fundo = pygame.image.load("imagens_jogo/fundo.png")
fundo = pygame.transform.scale(fundo,(constantes.LARGURA, constantes.ALTURA))

def mostrar_tela_nome(tela):

    pygame.display.set_caption("Aprova ou Reprova - Seleção de Nome")

    rodando = True

    fonte = pygame.font.SysFont(None,30)

    nome = ''

    while rodando:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                rodando = False

            
            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]

                elif evento.key == pygame.K_RETURN:
                    
                    if utils.valida_nome(nome) == True:
                        estado = 'tela_pergunta'
                        return nome, estado
                    else:
                        print("Nome Inválido")
            
                else:
                    nome += evento.unicode
            if evento.type == pygame.MOUSEBUTTONDOWN:

                if botao_confirma_nome.collidepoint(evento.pos):

                    if utils.valida_nome(nome) == True:
                        print("Nome confirmado!")
                        estado = 'tela_pergunta'
                        return nome, estado
                    else:
                        print("Nome Inválido")
                
                if botao_voltar.collidepoint(evento.pos):
                    estado = "menu_inicial"
                    return None,estado
            
        tela.fill(constantes.BRANCO)
        tela.blit(fundo,(0,0))
        texto_titulo = fonte_titulo.render(
            "DIGITE SEU NOME:",
            True,
            constantes.PRETO
        )
        tela.blit(texto_titulo, texto_titulo.get_rect(center = (1280//2, 120)))

        pygame.draw.rect(tela,constantes.AMARELO, botao_confirma_nome)

        texto_confirmar = fonte_botao.render(
            "Confirmar Nome",
            True,
            constantes.PRETO
        )
        tela.blit(texto_confirmar, (510, 325))

        pygame.draw.rect(tela,constantes.AMARELO, botao_voltar)

        texto_voltar = fonte_botao.render(
            "Voltar",
            True,
            constantes.PRETO
        )
        tela.blit(texto_voltar, (600, 445))
        texto = fonte.render(nome, True, constantes.PRETO)
        pygame.draw.rect(tela,constantes.AZUL_CLARO, espaco_nome)
        tela.blit(texto, texto.get_rect(center = (1280//2,230)))

        pygame.display.flip()
        
    pygame.quit()
    sys.exit()