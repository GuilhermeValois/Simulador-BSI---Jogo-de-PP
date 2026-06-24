import pygame
from interface import constantes

def tela_escolha(tela, nome, moedas):

    fundo = pygame.image.load("imagens/fundo_jogo.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    fonte_titulo = pygame.font.SysFont(None, 60)
    fonte_texto = pygame.font.SysFont(None, 40)

    
    botoes = []
    for i in range(1, 10):
        x = 400 + ((i-1) % 3) * 100
        y = 250 + ((i-1)//3) * 80
        botoes.append((i, pygame.Rect(x, y, 80, 60)))
    
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
        cabecalho = f" 👤 {nome}                   🪙 {moedas}"

        tela.fill(constantes.BRANCO)

        # Desenhar fundo
        tela.blit(fundo, (0, 0))

        # Cabeçalho
        texto_cabecalho = fonte_texto.render(cabecalho, True, constantes.BRANCO)
        tela.blit(texto_cabecalho, (350, 100))

        # Título
        texto_titulo = fonte_titulo.render("ESCOLHA O PERÍODO", True, constantes.AMARELO)
        tela.blit(texto_titulo, (400, 180))

        # Botões
        for i, rect in botoes:
            pygame.draw.rect(tela, constantes.AZUL, rect, border_radius=10)
            texto_botao = fonte_texto.render(str(i), True, constantes.BRANCO)
            tela.blit(texto_botao, texto_botao.get_rect(center=rect.center))
        
        pygame.display.flip()