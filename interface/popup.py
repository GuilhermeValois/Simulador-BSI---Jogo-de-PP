from interface import constantes
import pygame


def mostrar_aprovacao(tela,jogador):
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
                    estado = 'tela_pergunta'
                    return estado
        
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
    pygame.display.set_caption("Aprova ou Reprova-Popup de reprovação")
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
