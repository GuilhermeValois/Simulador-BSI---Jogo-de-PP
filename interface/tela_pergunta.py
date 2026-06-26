import pygame
from interface import constantes
from sistema import utils
import sys
from interface import popup


def mostrar_tela_pergunta(jogador,tela,perguntas_por_categoria,lista_disciplinas,periodo=None):
    pygame.init()

    fonte_disciplina = pygame.font.SysFont(None,40)
    fonte_botao = pygame.font.SysFont(None, constantes.TAMANHO_TEXTO)
    fonte_alternativas = pygame.font.SysFont("Segoe UI Symbol",20)
    fonte = pygame.font.SysFont(None,30)

    espaco_energia = pygame.Rect(540,20,200,30)

    botao_a = pygame.Rect(130, 250, 100, 100)
    espaco_a = pygame.Rect(250, 250, 350, 100)
    botao_b = pygame.Rect(720, 250, 100, 100)
    espaco_b = pygame.Rect(840, 250, 350, 100)
    botao_c = pygame.Rect(130, 480, 100, 100)
    espaco_c = pygame.Rect(250, 480, 350, 100)
    botao_d = pygame.Rect(720, 480, 100, 100)
    espaco_d = pygame.Rect(840, 480, 350, 100)

    pygame.display.set_caption("Aprova ou Reprova - Tela de pergunta")
    rodando = True   
    acertos = 0
    disciplinas_que_reprovou = [] 
    moedas = 0
    jogador.energia = jogador.energia_max
    decorrido = 0
    
    tempo_acabou = False
    
    if periodo == None:
        periodo_escolhido = jogador.periodo
    else:
        periodo_escolhido = periodo
    
    disciplinas = utils.disciplina_por_periodo(lista_disciplinas, periodo_escolhido, jogador.nome)
    if len(jogador.disciplinas_pendentes) > 0 and jogador.situacao == 'cursando':
        disciplinas.extend(jogador.disciplinas_pendente)
    elif len(jogador.disciplinas_pendentes) > 0 and jogador.situacao == 'concluindo_curso':
        popup.finalizando_curso
        disciplinas = jogador.disciplinas_pendentes
    for disciplina in disciplinas:
        segundos_decorridos = 0
        resposta = None
        pergunta = disciplina.sortear_pergunta_da_disciplina(perguntas_por_categoria)
        inicio = pygame.time.get_ticks()
        while rodando:
            if tempo_acabou:
                tempo_acabou = False
                mensagem = fonte.render("NÂO RESPONDIDA",True,constantes.VERMELHO)
                disciplinas_que_reprovou.append(disciplina)
                utils.contador(tela,fonte,3,mensagem)
                break
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
                    if restante >= 15:
                        jogador.energia += 20
                        if jogador.energia >= jogador.energia_max:
                            jogador.energia = jogador.energia_max
                    elif restante >=10:
                        jogador.energia += 10
                        if jogador.energia >= jogador.energia_max:
                            jogador.energia = jogador.energia_max
                    else:
                        jogador.energia += 5
                        if jogador.energia >= jogador.energia_max:
                            jogador.energia = jogador.energia_max
                    mensagem = fonte.render("RESPOSTA CORRETA",True,constantes.VERDE)
                    acertos += 1
                    if disciplina not in jogador.disciplinas_pendentes:
                        moedas += 10
                    utils.contador(tela,fonte,3,mensagem)
                    break
                else:
                    mensagem = fonte.render("RESPOSTA INCORRETA",True,constantes.VERMELHO)
                    disciplinas_que_reprovou.append(disciplina)
                    utils.contador(tela,fonte,3,mensagem)
                    break

            tela.fill(constantes.BRANCO)
            fundo = pygame.image.load("imagens/fundo_jogo.png")
            fundo = pygame.transform.scale(fundo, (1280, 720))
            tela.blit(fundo,(0,0))
            segundos = 20
            restante = segundos - (pygame.time.get_ticks() - inicio) // 1000

            if restante <= 0:
                tempo_acabou = True
                
            texto = fonte.render(f"CRONÔMETRO: {restante}",True,constantes.BRANCO)
            
            if restante != segundos_decorridos:
                segundos_decorridos = restante
                if (jogador.energia - 2) < 0:
                    jogador.energia = 0
                    decorrido +=1
                else:
                    jogador.energia -= 2
                    decorrido+=1
            if jogador.energia == 0:
                jogador.reprovacoes += 1
                estado = popup.mostrar_reprovacao(tela,jogador)     
                return estado

            tela.blit(texto,texto.get_rect(center=(130, 40)))
        
            texto_disciplina = fonte_disciplina.render(f"Disciplina: {disciplina.nome}",True,constantes.AMARELO)
            tela.blit(texto_disciplina, (texto_disciplina.get_rect(center=(1280//2, 80))))

            jogador_periodo = fonte.render(f"Período: {jogador.periodo}", True, constantes.BRANCO)
            tela.blit(jogador_periodo, (jogador_periodo.get_rect(center=(1280//2, 150))))

            quantidade_moedas = fonte.render(f"{moedas} moedas", True, constantes.AMARELO)
            tela.blit(quantidade_moedas,(1150,40))

            energia = fonte.render(f"ENERGIA: {jogador.energia}/{jogador.energia_max}",True, constantes.BRANCO)
            tela.blit(energia,(energia.get_rect(center = (450,35))))
            pygame.draw.rect(tela,constantes.VERMELHO,espaco_energia,border_radius=30)
            largura_energia = (jogador.energia / jogador.energia_max) * 200
            pygame.draw.rect(tela,constantes.VERDE,(540, 20, largura_energia, 30),border_radius=30)
            # Borda
            pygame.draw.rect(tela,constantes.PRETO,espaco_energia,2,border_radius=30)

            
            linhas = utils.quebrar_texto(pergunta.enunciado,fonte,1000)
            y = 180
            for linha in linhas:
                texto = fonte.render(linha,True,constantes.BRANCO)
                tela.blit(texto, (texto.get_rect(center = (1280//2,y))))
                y += 35

            #Alternativa A
            pygame.draw.rect(tela,constantes.AMARELO, botao_a,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,botao_a,2,border_radius=30)
            texto_a = fonte_botao.render(
                "A",
                True,
                constantes.PRETO
            )
            tela.blit(texto_a, (texto_a.get_rect(center=botao_a.center)))
            pygame.draw.rect(tela,constantes.VERDE, espaco_a,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,espaco_a,2,border_radius=30)

            linhas = utils.quebrar_texto(pergunta.alternativas['A'],fonte,350)
            y
            if len(linhas) == 1:
                y = 300
            elif len(linhas) == 2:
                y = 280
            else:
                y = 270
            for linha in linhas:
                texto = fonte_alternativas.render(linha,True,constantes.PRETO)
                tela.blit(texto, (texto.get_rect(center = (espaco_a.centerx,y))))
                y += 20
            #Alternativa B
            pygame.draw.rect(tela,constantes.AMARELO, botao_b,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,botao_b,2,border_radius=30)
            texto_b = fonte_botao.render(
                "B",
                True,
                constantes.PRETO
            )
            tela.blit(texto_b, (texto_b.get_rect(center=botao_b.center)))
            pygame.draw.rect(tela,constantes.VERDE, espaco_b,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,espaco_b,2,border_radius=30)

            linhas = utils.quebrar_texto(pergunta.alternativas['B'],fonte,350)
            y
            if len(linhas) == 1:
                y = 300
            elif len(linhas) == 2:
                y = 280
            else:
                y = 270
            for linha in linhas:
                texto = fonte_alternativas.render(linha,True,constantes.PRETO)
                tela.blit(texto, (texto.get_rect(center = (espaco_b.centerx,y))))
                y += 20
            #Alternativa C
            pygame.draw.rect(tela,constantes.AMARELO, botao_c,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,botao_c,2,border_radius=30)
            texto_c = fonte_botao.render(
                "C",
                True,
                constantes.PRETO
            )
            tela.blit(texto_c, (texto_c.get_rect(center=botao_c.center)))
            pygame.draw.rect(tela,constantes.VERDE, espaco_c,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,espaco_c,2,border_radius=30)
            
            linhas = utils.quebrar_texto(pergunta.alternativas['C'],fonte,350)
            y
            if len(linhas) == 1:
                y = 530
            elif len(linhas) == 2:
                y = 510
            else:
                y = 500
            for linha in linhas:
                texto = fonte_alternativas.render(linha,True,constantes.PRETO)
                tela.blit(texto, (texto.get_rect(center = (espaco_c.centerx,y))))
                y += 20
            #Alternativa D

            pygame.draw.rect(tela,constantes.AMARELO, botao_d,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,botao_d,2,border_radius=30)
            texto_d = fonte_botao.render(
                "D",
                True,
                constantes.PRETO
            )
            tela.blit(texto_d, (texto_d.get_rect(center=botao_d.center)))
            pygame.draw.rect(tela,constantes.VERDE, espaco_d,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,espaco_d,2,border_radius=30)
            
            linhas = utils.quebrar_texto(pergunta.alternativas['D'],fonte,350)
            y
            if len(linhas) == 1:
                y = 530
            elif len(linhas) == 2:
                y = 510
            else:
                y = 500
            for linha in linhas:
                texto = fonte_alternativas.render(linha,True,constantes.PRETO)
                tela.blit(texto, (texto.get_rect(center = (espaco_d.centerx,y))))
                y += 20
            pygame.display.flip()
    if acertos >= len(disciplinas)/2:
        if len(disciplinas_que_reprovou) > 0:
            jogador.disciplinas_pendentes = disciplinas_que_reprovou
            estado = popup.pagar_pendencias(tela,jogador)
            if periodo == 8: jogador.situacao = 'concluindo_curso'
            if jogador.periodo < 8:jogador.passou_de_periodo()
            jogador.moedas += moedas
            jogador.periodo_desbloqueado += 1
            estado = 'tela de escolha'
            return estado
        else:
            if periodo == 8: 
                jogador.situacao = 'formado'
                utils.gerar_certificado(jogador.nome)
            if jogador.periodo < 8:jogador.passou_de_periodo()
            jogador.disciplinas_pendentes = []
            jogador.moeda = moedas
            jogador.periodo_desbloqueado += 1
            estado = popup.mostrar_aprovacao(tela, jogador)
            return estado
    else:
        jogador.reprovacoes += 1
        estado = popup.mostrar_reprovacao(tela,jogador)     
        return estado
    