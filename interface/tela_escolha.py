import pygame
from interface import constantes

def tela_escolha(tela,jogador):

    fundo = pygame.image.load("imagens/fundo_jogo.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    fonte_emoji = pygame.font.SysFont("Segoe UI Emoji", 40)
    fonte_texto = pygame.font.SysFont("arial black", 40, bold=True)
    fonte_cabecalho = pygame.font.SysFont("arial", 40, bold=True)

    botoes = []
    largura_botao = 300
    altura_botao = 300
    espacamento_x = 50
    espacamento_y = 40
    inicio_x = 150
    inicio_y = 250

    for i in range(8):
        linha = i // 3
        coluna = i % 3
        x = inicio_x + coluna * (largura_botao + espacamento_x)
        y = inicio_y + linha * (altura_botao + espacamento_y)
        botoes.append((i+1, pygame.Rect(x, y, largura_botao, altura_botao)))
    
    # Imagem períodos
    imagem_periodos = []
    for i in range(8):
        fundo_periodo = pygame.image.load(f"imagens/fundo_periodos.png")
        fundo_periodo = pygame.transform.scale(fundo_periodo, (300, 300))
        imagem_periodos.append(fundo_periodo)
    
    jogador.periodo_desbloqueado = 1
    scroll_y = 0
    limite_superior = 0
    limite_inferior = -((len(botoes)//3) * (altura_botao + espacamento_y) - 300 + 150)
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 4:
                    scroll_y = min(scroll_y + 40, limite_superior)
                elif evento.button == 5:
                    scroll_y = max(scroll_y - 40, limite_inferior)
                else:
                    for i, rect in botoes:
                        rect_scroll = rect.move(0, scroll_y)
                        if rect_scroll.collidepoint(evento.pos):
                            if i <= jogador.periodo_desbloqueado:
                                print(f"Período escolhido: {i}º")
                                return i, 'minigame'
                            else:
                                print("Período bloqueado")

        tela.fill(constantes.BRANCO)

        # Desenhar fundo
        tela.blit(fundo, (0, 0))

        # Cabeçalho
        texto_emoji_nome = fonte_emoji.render("👤", True, constantes.BRANCO)
        texto_nome = fonte_cabecalho.render(jogador.nome, True, constantes.BRANCO)
        tela.blit(texto_emoji_nome, (140, 70 + scroll_y))
        tela.blit(texto_nome, (190, 70 + scroll_y))

        texto_emoji_moeda = fonte_emoji.render("🪙", True, constantes.BRANCO)
        texto_moeda = fonte_cabecalho.render(f"{jogador.moedas} moedas", True, constantes.BRANCO)
        tela.blit(texto_emoji_moeda, (940, 70 + scroll_y))
        tela.blit(texto_moeda, (1000, 70 + scroll_y))

        # Título
        texto_titulo_sombra = fonte_texto.render("ESCOLHA O PERÍODO", True, constantes.CINZA_ESCURO)
        texto_titulo = fonte_texto.render("ESCOLHA O PERÍODO", True, constantes.AMARELO)
        tela.blit(texto_titulo_sombra, (410,75 + scroll_y))
        tela.blit(texto_titulo, (410, 70 + scroll_y))

        # Botões
        for i, rect in botoes:
            rect_scroll = rect.move(0, scroll_y)
            tela.blit(imagem_periodos[i-1], rect_scroll)

            # Bloqueado
            if i > jogador.periodo_desbloqueado:
                cadeado = fonte_emoji.render("🔒", True, constantes.VERMELHO)
                cadeado_rect = cadeado.get_rect(center=rect_scroll.center)
                tela.blit(cadeado, cadeado_rect)
            
            #Desbloqueado
            else:
                pygame.draw.rect(tela, constantes.AMARELO, rect_scroll, 3, border_radius=10)
                texto_botao_sombra = fonte_texto.render(f"{i}º período", True, constantes.CINZA_ESCURO)
                texto_emoji = fonte_emoji.render("📚", True, constantes.BRANCO)
                texto_botao = fonte_texto.render(f" {i}º período", True, constantes.AMARELO)
        
                # Combinar emoji e texto
                largura_total = texto_emoji.get_width() + texto_botao.get_width() + 10
                x_base = rect_scroll.centerx - largura_total // 2
                y_base = rect_scroll.centery - texto_botao.get_height() // 2

                emoji_rect = texto_emoji.get_rect(center=(rect_scroll.centerx, rect_scroll.centery - 40))
                texto_rect = texto_botao.get_rect(center=(rect_scroll.centerx, rect_scroll.centery + 40))

                tela.blit(texto_botao_sombra, (texto_rect.x + 2, texto_rect.y + 2))
                tela.blit(texto_emoji, emoji_rect)
                tela.blit(texto_botao, texto_rect)
        
        pygame.display.flip()