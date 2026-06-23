import pygame
from interface import constantes
from sistema import utils
import sys

pygame.init()

fonte_disciplina = pygame.font.SysFont(None,40)
fonte_botao = pygame.font.SysFont(None, constantes.TAMANHO_TEXTO)
fonte_alternativas = pygame.font.SysFont("Segoe UI Symbol",20)
fonte = fonte_disciplina = pygame.font.SysFont(None,30)

botao_a = pygame.Rect(130, 250, 100, 100)
espaco_a = pygame.Rect(250, 250, 350, 100)
botao_b = pygame.Rect(720, 250, 100, 100)
espaco_b = pygame.Rect(840, 250, 350, 100)
botao_c = pygame.Rect(130, 480, 100, 100)
espaco_c = pygame.Rect(250, 480, 350, 100)
botao_d = pygame.Rect(720, 480, 100, 100)
espaco_d = pygame.Rect(840, 480, 350, 100)

def mostrar_tela_pergunta(jogador,tela,perguntas_por_categoria,lista_disciplinas):

    pygame.display.set_caption("Aprova ou Reprova - Tela de pergunta")
    rodando = True
    while jogador.periodo <= 8:
        if len(jogador.disciplinas_pendentes):
            estado = 'tela_pagar_pendencias'
            return estado
        acertos = 0
        disciplinas_que_reprovou = [] 
        disciplinas = utils.disciplina_por_periodo(lista_disciplinas, jogador.periodo, jogador.nome)
        for disciplina in disciplinas:
            resposta = None
            pergunta = disciplina.sortear_pergunta_da_disciplina(perguntas_por_categoria)
            while rodando:
        
                for evento in pygame.event.get():

                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if evento.type == pygame.MOUSEBUTTONDOWN:

                        if botao_a.collidepoint(evento.pos):
                            resposta = 'A'

                        if botao_b.collidepoint(evento.pos):
                            resposta = 'B'

                        if botao_c.collidepoint(evento.pos):
                            resposta = 'C'
 
                        if botao_d.collidepoint(evento.pos):
                            resposta = 'D'
            
                if resposta in ['A','B','C','D']: 
                    if resposta == pergunta.resposta:
                        mensagem = fonte.render("RESPOSTA CORRETA",True,constantes.VERDE)
                        acertos += 1
                        utils.contador(tela,fonte,3,mensagem)
                        break
                    else:
                        mensagem = fonte.render("RESPOSTA INCORRETA",True,constantes.VERMELHO)
                        disciplinas_que_reprovou.append(disciplina)
                        utils.contador(tela,fonte,3,mensagem)
                        break

                tela.fill(constantes.BRANCO)
                texto_disciplina = fonte_disciplina.render(f"Disciplina: {disciplina.nome}",True,constantes.PRETO)
                tela.blit(texto_disciplina, (texto_disciplina.get_rect(center=(1280//2, 80))))

                nome_jogador = fonte.render(f"Aluno: {jogador.nome}", True, constantes.PRETO)
                tela.blit(nome_jogador, (nome_jogador.get_rect(center=(1280//2, 120))))

                jogador_periodo = fonte.render(f"Período: {jogador.periodo}", True, constantes.PRETO)
                tela.blit(jogador_periodo, (jogador_periodo.get_rect(center=(1280//2, 150))))

                linhas = utils.quebrar_texto(pergunta.enunciado,fonte,1000)
                y = 180
                for linha in linhas:
                    texto = fonte.render(linha,True,constantes.PRETO)
                    tela.blit(texto, (texto.get_rect(center = (1280//2,y))))
                    y += 35

                #Alternativa A
                pygame.draw.rect(tela,constantes.AMARELO, botao_a)
                texto_a = fonte_botao.render(
                    "A",
                    True,
                    constantes.PRETO
                )
                tela.blit(texto_a, (texto_a.get_rect(center=botao_a.center)))
                pygame.draw.rect(tela,constantes.VERDE, espaco_a)
            
                linhas = utils.quebrar_texto(pergunta.alternativas['A'],fonte,350)
                y
                if len(linhas) == 1:
                    y = 300
                elif len(linhas) == 2:
                    y = 280
                else:
                    y = 260
                for linha in linhas:
                    texto = fonte_alternativas.render(linha,True,constantes.PRETO)
                    tela.blit(texto, (texto.get_rect(center = (espaco_a.centerx,y))))
                    y += 20
                #Alternativa B
                pygame.draw.rect(tela,constantes.AMARELO, botao_b)
                texto_b = fonte_botao.render(
                    "B",
                    True,
                    constantes.PRETO
                )
                tela.blit(texto_b, (texto_b.get_rect(center=botao_b.center)))
                pygame.draw.rect(tela,constantes.VERDE, espaco_b)

                linhas = utils.quebrar_texto(pergunta.alternativas['B'],fonte,350)
                y
                if len(linhas) == 1:
                    y = 300
                elif len(linhas) == 2:
                    y = 280
                else:
                    y = 260
                for linha in linhas:
                    texto = fonte_alternativas.render(linha,True,constantes.PRETO)
                    tela.blit(texto, (texto.get_rect(center = (espaco_b.centerx,y))))
                    y += 20
                #Alternativa C
                pygame.draw.rect(tela,constantes.AMARELO, botao_c)
                texto_c = fonte_botao.render(
                    "C",
                    True,
                    constantes.PRETO
                )
                tela.blit(texto_c, (texto_a.get_rect(center=botao_c.center)))
                pygame.draw.rect(tela,constantes.VERDE, espaco_c)
            
                linhas = utils.quebrar_texto(pergunta.alternativas['C'],fonte,350)
                y
                if len(linhas) == 1:
                    y = 530
                elif len(linhas) == 2:
                    y = 510
                else:
                    y = 490
                for linha in linhas:
                    texto = fonte_alternativas.render(linha,True,constantes.PRETO)
                    tela.blit(texto, (texto.get_rect(center = (espaco_c.centerx,y))))
                    y += 20
                #Alternativa D

                pygame.draw.rect(tela,constantes.AMARELO, botao_d)
                texto_d = fonte_botao.render(
                    "D",
                    True,
                    constantes.PRETO
                )
                tela.blit(texto_d, (texto_a.get_rect(center=botao_d.center)))
                pygame.draw.rect(tela,constantes.VERDE, espaco_d)
            
                linhas = utils.quebrar_texto(pergunta.alternativas['D'],fonte,350)
                y
                if len(linhas) == 1:
                    y = 530
                elif len(linhas) == 2:
                    y = 510
                else:
                    y = 490
                for linha in linhas:
                    texto = fonte_alternativas.render(linha,True,constantes.PRETO)
                    tela.blit(texto, (texto.get_rect(center = (espaco_d.centerx,y))))
                    y += 20
                pygame.display.flip()
        if acertos >= len(disciplinas)//2:
            jogador.disciplinas_pendentes.extend(disciplinas_que_reprovou)
            jogador.passou_de_periodo()
        else:
            continue
    pygame.quit()
    sys.exit()