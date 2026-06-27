from interface import constantes
import pygame
import sys
from sistema import utils

def mostrar_aprovacao(tela, jogador):
    pygame.init()
    pygame.display.set_caption("Aprova ou Reprova-Popup de aprovação")
    popup = pygame.Rect(465,200,350,120)
    botao_menu = pygame.Rect(440,360,400,80)
    botao_avancar = pygame.Rect(490,490,300,80)
    fonte_mensagem = pygame.font.SysFont(None, 22)
    fonte_botao = pygame.font.Font(None, 30)
    
    rodando = True

    while rodando:

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                
                if botao_menu.collidepoint(evento.pos):
                    estado = 'tela_escolha'
                    return estado
                if botao_avancar.collidepoint(evento.pos):
                    return 'minigame'
        
        tela.fill(constantes.AZUL_CLARO)
        fundo = pygame.image.load("imagens/fundo_aprovado.png")
        fundo = pygame.transform.scale(fundo, (1280, 720))
        tela.blit(fundo,(0,0))
        pygame.draw.rect(tela,constantes.VERDE,botao_menu,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,botao_menu,2,border_radius=30)
        pygame.draw.rect(tela,constantes.BRANCO,popup,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,popup,2,border_radius=30)
        pygame.draw.rect(tela,constantes.VERDE,botao_avancar,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,botao_avancar,2,border_radius=30)
        texto_avancar = fonte_botao.render("PRÓXIMO PERÍODO", True, constantes.PRETO)
        tela.blit(texto_avancar, (texto_avancar.get_rect(center = botao_avancar.center)))
        texto_voltar = fonte_botao.render("VOLTAR PARA MENU DE ESCOLHAS", True, constantes.PRETO)
        tela.blit(texto_voltar, (texto_voltar.get_rect(center = botao_menu.center)))
        texto_parabens = fonte_mensagem.render("PARABÉNS! VOCÊ FOI APROVADO", True, constantes.PRETO)
        texto_desbloqueio = fonte_mensagem.render(f"{jogador.periodo}° PERÍODO AGORA ESTÁ DESBLOQUEADO", True, constantes.PRETO)
        texto_menu = fonte_mensagem.render("EM MENU DE ESCOLHAS", True, constantes.PRETO)
        tela.blit(texto_parabens, (texto_parabens.get_rect(center = (popup.centerx,240))))
        tela.blit(texto_desbloqueio, (texto_desbloqueio.get_rect(center = (popup.centerx,260))))
        tela.blit(texto_menu, (texto_menu.get_rect(center = (popup.centerx,280))))
        pygame.display.flip()
def mostrar_reprovacao(tela,jogador):

    pygame.init()
    pygame.display.set_caption("Aprova ou Reprova-Popup de Reprovação")
    popup = pygame.Rect(465,200,350,120)
    botao_menu = pygame.Rect(440,360,400,80)
    botao_refazer = pygame.Rect(490,490,300,80)
    fonte_mensagem = pygame.font.SysFont(None, 22)
    fonte_botao = pygame.font.Font(None, 30)
    
    rodando = True

    while rodando:

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                
                if botao_menu.collidepoint(evento.pos):
                    estado = 'tela_escolha'
                    return estado
                if botao_refazer.collidepoint(evento.pos):
                    estado = 'tela_pergunta'
                    return estado
        tela.fill(constantes.AZUL_CLARO)
        fundo = pygame.image.load("imagens/fundo_reprovado.png")
        fundo = pygame.transform.scale(fundo, (1280, 720))
        tela.blit(fundo,(0,0))
        pygame.draw.rect(tela,constantes.VERDE,botao_menu,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,botao_menu,2,border_radius=30)
        pygame.draw.rect(tela,constantes.VERDE,botao_refazer,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,botao_refazer,2,border_radius=30)
        pygame.draw.rect(tela,constantes.BRANCO,popup,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,popup,2,border_radius=30)
        texto_refazer = fonte_botao.render("REFAZER PERÍODO", True, constantes.PRETO)
        tela.blit(texto_refazer, (texto_refazer.get_rect(center = botao_refazer.center)))
        texto_voltar = fonte_botao.render("VOLTAR PARA MENU DE ESCOLHAS", True, constantes.PRETO)
        tela.blit(texto_voltar, (texto_voltar.get_rect(center = botao_menu.center)))
        texto_que_pena = fonte_mensagem.render("QUE PENA! VOCÊ FOI REPROVADO", True, constantes.PRETO)
        texto_paga = fonte_mensagem.render(f"PAGARÁ O {jogador.periodo}° PERÍODO NOVAMENTE", True, constantes.PRETO)
        texto_menu = fonte_mensagem.render("EM MENU DE ESCOLHAS", True, constantes.PRETO)
        tela.blit(texto_que_pena, (texto_que_pena.get_rect(center = (popup.centerx,240))))
        tela.blit(texto_paga, (texto_paga.get_rect(center = (popup.centerx,260))))
        tela.blit(texto_menu, (texto_menu.get_rect(center = (popup.centerx,280))))
        pygame.display.flip()

def pagar_pendencias(tela,jogador):

    pygame.init()

    fundo = pygame.image.load("imagens/fundo_jogo.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    fonte = pygame.font.SysFont(None, 22)
    fonte_mensagem = pygame.font.SysFont(None, 50)
    fonte_titulo = pygame.font.SysFont(None, 50)
    fonte_botao = pygame.font.SysFont(None,40)
    pygame.display.set_caption("Aprova ou Reprova-Popup de Pendências")
    botoes_pendencias = []

    y = 250
    for disciplina in jogador.disciplinas_pendentes:
        botao = pygame.Rect(805, y-10, 120, 40)
        botao_enfeite = pygame.Rect(335, y-10, 590, 40)
        y += 60
        botoes_pendencias.append((botao_enfeite,botao, disciplina))
    botao_moedas = pygame.Rect(30, 20, 250, 30)
    botao_mensagem = pygame.Rect(280, 335, 720, 50)
    botao_titulo = pygame.Rect(415, 20, 450, 50)
    botao_voltar = pygame.Rect(290, 580, 350, 80)
    botao_avancar = pygame.Rect(670, 580, 300, 80)
    rodando  = True

    while rodando:
 
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:

                for botao_enfeite, botao, disciplina in botoes_pendencias:

                    if botao.collidepoint(evento.pos):

                        if jogador.moedas >= 10:

                            jogador.moedas -= 10
                            jogador.disciplinas_pendentes.remove(disciplina)
                            botoes_pendencias = []
                            y = 250
                            for disciplina in jogador.disciplinas_pendentes:
                                botao = pygame.Rect(805, y-10, 120, 40)
                                botao_enfeite = pygame.Rect(335, y-10, 590, 40)
                                y += 60
                                botoes_pendencias.append((botao_enfeite, botao, disciplina))
                            break
                if botao_voltar.collidepoint(evento.pos):
                    estado = 'tela_escolha'
                    return estado
                if botao_avancar.collidepoint(evento.pos):
                    jogador.passou_de_periodo()
                    return 'minigame'

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.fill(constantes.BRANCO)
        pygame.draw.rect(tela,constantes.AMARELO,botao_titulo,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,botao_titulo,2,border_radius=30)
        titulo = fonte_titulo.render("PAGAR PENDÊNCIAS", True, constantes.PRETO)
        tela.blit(titulo, (titulo.get_rect(center = (botao_titulo.center))))
        tela.blit(fundo, (0, 0))

        mensagem = fonte_mensagem.render("Custo por pendência: 10 moedas",True,constantes.PRETO)
        tela.blit(mensagem, (mensagem.get_rect(center = (constantes.LARGURA//2,180))))
        pygame.draw.rect(tela, constantes.AMARELO, botao_voltar, border_radius=30)
        pygame.draw.rect(tela, constantes.PRETO, botao_voltar, 2, border_radius=30)

        pygame.draw.rect(tela, constantes.AMARELO, botao_avancar, border_radius=30)
        pygame.draw.rect(tela, constantes.PRETO, botao_avancar, 2, border_radius=30)

        texto_menu = fonte_botao.render("MENU DE ESCOLHAS", True, constantes.PRETO)
        texto_avancar = fonte_botao.render("AVANÇAR", True, constantes.PRETO)

        tela.blit(texto_menu, texto_menu.get_rect(center=botao_voltar.center))
        tela.blit(texto_avancar, texto_avancar.get_rect(center=botao_avancar.center))
        y = 250
        for botao_enfeite,botao,disciplina in botoes_pendencias:

            if disciplina in jogador.disciplinas_pendentes:

                pygame.draw.rect(tela, constantes.LARANJA, botao_enfeite,border_radius=30)
                texto = fonte.render(disciplina.nome, True, constantes.PRETO)
                tela.blit(texto, (355, y))

                
                pygame.draw.rect(tela, constantes.VERDE, botao,border_radius=30)

                texto_botao = fonte.render("Pagar", True, constantes.PRETO)
                tela.blit(texto_botao, (texto_botao.get_rect(center=(botao.center))))
                y += 60
        pygame.draw.rect(tela,constantes.AMARELO,botao_moedas,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,botao_moedas,2,border_radius=30)
        quantidade_moedas = fonte.render(f"MOEDAS DISPONÍVEIS: {jogador.moedas}", True, constantes.PRETO)
        tela.blit(quantidade_moedas, (quantidade_moedas.get_rect(center = (botao_moedas.center))))
        if len(botoes_pendencias) == 0:
            pygame.draw.rect(tela,constantes.AMARELO,botao_mensagem,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,botao_mensagem,2,border_radius=30)
            mensagem = fonte_mensagem.render("TODAS AS PENDÊNCIAS FORAM PAGAS", True, constantes.PRETO)
            tela.blit(mensagem, (mensagem.get_rect(center = (constantes.LARGURA//2,constantes.ALTURA//2))))
        pygame.display.flip()

def finalizando_curso(tela,jogador):

    pygame.init()
    fonte = pygame.font.SysFont(None, 22)
    fonte_mensagem = pygame.font.SysFont(None, 50)
    fonte_titulo = pygame.font.SysFont(None, 50)
    fonte_botao = pygame.font.SysFont(None,40)
    pygame.display.set_caption("Aprova ou Reprova-Popup de Pendências")
    botoes_pendencias = []
    y = 250
    for disciplina in jogador.disciplinas_pendentes:
        botao = pygame.Rect(805, y-10, 120, 40)
        botao_enfeite = pygame.Rect(335, y-10, 590, 40)
        y += 60
        botoes_pendencias.append((botao_enfeite,botao, disciplina))
    botao_moedas = pygame.Rect(30, 20, 250, 30)
    botao_mensagem = pygame.Rect(280, 335, 720, 50)
    botao_titulo = pygame.Rect(415, 20, 450, 50)
    botao_voltar = pygame.Rect(290, 580, 350, 80)
    botao_avancar = pygame.Rect(670, 580, 300, 80)
    rodando  = True

    while rodando:
 
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:

                for botao_enfeite, botao, disciplina in botoes_pendencias:

                    if botao.collidepoint(evento.pos):

                        if jogador.moedas >= 10:

                            jogador.moedas -= 10
                            jogador.disciplinas_pendentes.remove(disciplina)
                            botoes_pendencias = []
                            y = 250
                            for disciplina in jogador.disciplinas_pendentes:
                                botao = pygame.Rect(805, y-10, 120, 40)
                                botao_enfeite = pygame.Rect(335, y-10, 590, 40)
                                y += 60
                                botoes_pendencias.append((botao_enfeite, botao, disciplina))
                            break
                if botao_voltar.collidepoint(evento.pos):
                    estado = 'tela_escolha'
                    return estado
                if botao_avancar.collidepoint(evento.pos):
                    jogador.passou_de_periodo()
                    return 'minigame'

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.fill(constantes.AZUL_CLARO)
        pygame.draw.rect(tela,constantes.AMARELO,botao_titulo,border_radius=30)
        pygame.draw.rect(tela,constantes.BRANCO,botao_titulo,2,border_radius=30)
        
        titulo = fonte_titulo.render("FINALIZAÇÃO DO CURSO",True,constantes.PRETO)
        tela.blit(titulo, (titulo.get_rect(center = (botao_titulo.center))))
        mensagem = fonte_mensagem.render("Pague as últimas pendências para concluir o curso!",True,constantes.PRETO)
        tela.blit(mensagem, (mensagem.get_rect(center = (constantes.LARGURA//2,110))))
        mensagem = fonte_mensagem.render("Custo por pendência: 10 moedas",True,constantes.PRETO)
        tela.blit(mensagem, (mensagem.get_rect(center = (constantes.LARGURA//2,180))))
        
        pygame.draw.rect(tela, constantes.VERDE, botao_voltar, border_radius=30)
        pygame.draw.rect(tela, constantes.PRETO, botao_voltar, 2, border_radius=30)

        pygame.draw.rect(tela, constantes.AMARELO, botao_avancar, border_radius=30)
        pygame.draw.rect(tela, constantes.PRETO, botao_avancar, 2, border_radius=30)

        texto_menu = fonte_botao.render("MENU DE ESCOLHAS", True, constantes.PRETO)
        texto_avancar = fonte_botao.render("AVANÇAR", True, constantes.PRETO)

        tela.blit(texto_menu, texto_menu.get_rect(center=botao_voltar.center))
        tela.blit(texto_avancar, texto_avancar.get_rect(center=botao_avancar.center))
        y = 250
        for botao_enfeite,botao,disciplina in botoes_pendencias:

            if disciplina in jogador.disciplinas_pendentes:

                pygame.draw.rect(tela, constantes.LARANJA, botao_enfeite,border_radius=30)
                texto = fonte.render(disciplina.nome, True, constantes.PRETO)
                tela.blit(texto, (355, y))

                
                pygame.draw.rect(tela, constantes.PRETO, botao,border_radius=30)

                texto_botao = fonte.render("Pagar", True, constantes.PRETO)
                tela.blit(texto_botao, (texto_botao.get_rect(center=(botao.center))))
                y += 60
        pygame.draw.rect(tela,constantes.AMARELO,botao_moedas,border_radius=30)
        pygame.draw.rect(tela,constantes.PRETO,botao_moedas,2,border_radius=30)
        quantidade_moedas = fonte.render(f"MOEDAS DISPONÍVEIS: {jogador.moedas}", True, constantes.PRETO)
        tela.blit(quantidade_moedas, (quantidade_moedas.get_rect(center = (botao_moedas.center))))
        if len(botoes_pendencias) == 0:
            utils.gerar_certificado(jogador.nome)
            pygame.draw.rect(tela,constantes.AMARELO,botao_mensagem,border_radius=30)
            pygame.draw.rect(tela,constantes.PRETO,botao_mensagem,2,border_radius=30)
            mensagem = fonte_mensagem.render("TODAS AS PENDÊNCIAS FORAM PAGAS", True, constantes.PRETO)
            tela.blit(mensagem, (mensagem.get_rect(center = (constantes.LARGURA//2,constantes.ALTURA//2))))

            return 'mostrar_aprovacao'
        
        pygame.display.flip()