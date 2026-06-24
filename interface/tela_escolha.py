import pygame
from interface import constantes

def tela_escolha(tela,jogador):

    fundo = pygame.image.load("imagens/fundo_jogo.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    fonte_titulo = pygame.font.SysFont(None, 60)
    fonte_texto = pygame.font.SysFont("Segoe UI Emoji", 40)

    cabecalho = f" 👤 {nome}                                                                            🪙 {moedas} moedas"

    botoes = []
    largura_botao = 300
    altura_botao = 300
    espacamento_x = 50
    espacamento_y = 40
    inicio_x = 150
    inicio_y = 250

    for i in range(9):
        linha = i // 3
        coluna = i % 3
        x = inicio_x + coluna * (largura_botao + espacamento_x)
        y = inicio_y + linha * (altura_botao + espacamento_y)
        botoes.append((i+1, pygame.Rect(x, y, largura_botao, altura_botao)))
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in botoes:
                    if rect.collidepoint(evento.pos):
                        print(f"Período escolhido: {i}")
                        return i, "tela_pergunta"
        cabecalho = f" 👤 {jogador.nome}                   🪙 {jogador.moedas}"

        tela.fill(constantes.BRANCO)

        # Desenhar fundo
        tela.blit(fundo, (0, 0))

        # Cabeçalho
        texto_cabecalho = fonte_texto.render(cabecalho, True, constantes.BRANCO)
        tela.blit(texto_cabecalho, (35, 100))

        # Título
        texto_titulo = fonte_titulo.render("ESCOLHA O PERÍODO", True, constantes.AMARELO)
        tela.blit(texto_titulo, (450, 100))

        # Botões
        for i, rect in botoes:
            pygame.draw.rect(tela, constantes.AZUL, rect, border_radius=10)
            texto_botao = fonte_texto.render(str(i), True, constantes.BRANCO)
            tela.blit(texto_botao, texto_botao.get_rect(center=rect.center))
        
        pygame.display.flip()