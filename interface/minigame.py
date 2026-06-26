import pygame
import sys
from interface import constantes
import random

caca_palavras = {
    1: ["determinacao", "logica", "estudo", "jogo"],
    2: ["programar", "papel", "avaliacao", "departamento"],
    3: ["ler", "python", "sustentavel", "escrita"],
    4: ["nota", "boletim", "principal", "material"],
    5: ["vaga", "conjunto", "aluno", "bolsa"],
    6: ["gestao", "computador", "aprova", "amizade"],
    7: ["reprova", "comunidade", "opcao", "curso"],
    8: ["aula", "administracao", "prova", "assunto"]
}

direcoes = ["horizontal", "vertical"]

def gerar_grade(periodo, tamanho=15):

    palavras = caca_palavras[periodo]
    grade = [["" for _ in range(tamanho)] for _ in range(tamanho)]

    for palavra in palavras:
        colocado = False
        while not colocado:
            direcao = random.choice(direcoes)

            if direcao == "horizontal":
                linha = random.randint(0, tamanho - 1)
                coluna = random.randint(0, tamanho-len(palavra))
                if all(grade[linha][coluna + i] in ["", palavra[i].upper()] for i in range(len(palavra))):
                    for i, letra in enumerate(palavra.upper()):
                        grade[linha][coluna + i] = letra
                    colocado = True
            
            elif direcao == "vertical":
                linha = random.randint(0, tamanho - len(palavra))
                coluna = random.randint(0, tamanho-1)
                if all(grade[linha + i][coluna] in ["", palavra[i].upper()] for i in range(len(palavra))):
                    for i, letra in enumerate(palavra.upper()):
                        grade[linha + i][coluna] = letra
    
    for i in range(tamanho):
        for j in range(tamanho):
            if grade[i][j] == "":
                grade[i][j] = chr(random.randint(65, 90))
    
    return grade

def desenhar_grade(tela, grade, fonte_texto, offset_x, offset_y, largura_celula, altura_celula, selecionando, palavras_coords):

    largura_grade = len(grade[0]) * largura_celula
    altura_grade = len(grade) * altura_celula

    # Fundo branco do minigame
    fundo_grande = pygame.Rect(offset_x, offset_y, largura_grade, altura_grade)
    pygame.draw.rect(tela, constantes.BRANCO, fundo_grande)

    for i, linha in enumerate(grade):
        for j, letra in enumerate(linha):
            rect = pygame.Rect(offset_x + j*largura_celula, offset_y + i*altura_celula, largura_celula, altura_celula)

            # Célula selecionada
            if (i, j) in selecionando:
                pygame.draw.rect(tela, constantes.AMARELO, rect)
            elif any ((i, j) in coords for coords in palavras_coords):
                pygame.draw.rect(tela, constantes.VERDE, rect)
            else:
                pygame.draw.rect(tela, constantes.BRANCO, rect)

            pygame.draw.rect(tela, constantes.PRETO, rect, 2)
            texto = fonte_texto.render(letra, True, constantes.PRETO)
            tela.blit(texto, texto.get_rect(center=rect.center))

def minigame(tela, jogador, periodo):

    fundo = pygame.image.load("imagens/fundo_jogo.png")
    fundo = pygame.transform.scale(fundo, (1280, 720))
    fonte_titulo = pygame.font.SysFont("arial black", 40, bold=True)
    fonte_texto = pygame.font.SysFont("arial", 40, bold=True)
    fonte_emoji = pygame.font.SysFont("Segoe UI Emoji", 40)
    fonte_lista = pygame.font.SysFont("arial", 15, bold=True)

    palavras = caca_palavras[periodo]
    grade = gerar_grade(periodo)
    palavras_encontradas = []
    selecionando = []
    palavras_coords = []

    # Tamanhos
    largura_celula = 60
    altura_celula = 40
    largura_grade = len(grade[0]) * largura_celula
    altura_grade = len(grade) * altura_celula

    # Ajuste horizontal e vertical
    offset_x = (constantes.LARGURA - largura_grade) // 2
    offset_y = 120


    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 'tela_escolha'
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                selecionando.clear()
                pos = pygame.mouse.get_pos()
                selecionar_letras(pos, grade, palavras_encontradas, palavras, offset_x, offset_y, largura_celula, altura_celula, selecionando)
            
            if evento.type == pygame.MOUSEMOTION and evento.buttons[0]:
                pos = pygame.mouse.get_pos()
                selecionar_letras(pos, grade, palavras_encontradas, palavras, offset_x, offset_y, largura_celula, altura_celula, selecionando)
            
            if evento.type == pygame.MOUSEBUTTONUP:
                if selecionando:
                    linhas = [l for l, c in selecionando]
                    colunas = [c for l, c in selecionando]

                    if (all(l == linhas[0] for l in linhas)or
                        all(c == colunas[0] for c in colunas)or
                        all(l - linhas[0] == c - colunas[0] for l, c in selecionando)):

                        palavra_formada = "".join(grade[l][c] for l, c in selecionando).lower()
                        if palavra_formada in palavras and palavra_formada not in palavras_encontradas:
                            palavras_encontradas.append(palavra_formada)
                            palavras_coords.append(list(selecionando))
                            print(f"Encontrou: {palavra_formada}")
                selecionando.clear()
                
        
        tela.blit(fundo, (0, 0))
        desenhar_grade(tela, grade, fonte_texto, offset_x, offset_y, largura_celula, altura_celula, selecionando, palavras_coords)

        texto_titulo_sombra = fonte_titulo.render("CAÇA-PALAVRAS", True, constantes.CINZA_ESCURO)
        texto_titulo = fonte_titulo.render("CAÇA-PALAVRAS", True, constantes.AMARELO)
        tela.blit(texto_titulo_sombra, (450, 35))
        tela.blit(texto_titulo, (450, 30))

        texto_emoji_moeda = fonte_emoji.render("🪙", True, constantes.BRANCO)
        texto_moeda = fonte_texto.render(f"{jogador.moedas} moedas", True, constantes.BRANCO)
        tela.blit(texto_emoji_moeda, (940, 50))
        tela.blit(texto_moeda, (1000, 50))

        texto = fonte_texto.render(f"{len(palavras_encontradas)} / {len(palavras)} encontradas", True, constantes.BRANCO)
        tela.blit(texto, (50, 50))

        texto_lista = fonte_lista.render("Palavras:", True, constantes.AMARELO)
        tela.blit(texto_lista, (40, 150))

        for idx, palavra in enumerate(palavras):
            cor = constantes.BRANCO
            if palavra in palavras_encontradas:
                cor = constantes.VERDE
            texto_palavra = fonte_lista.render(palavra.upper(), True, cor)
            tela.blit(texto_palavra, (40, 200 + idx * 40))

        pygame.display.flip()

        if len(palavras_encontradas) == len(palavras):
            return 'tela_pergunta'

def selecionar_letras(pos, grade, palavras_encontradas, palavras, offset_x, offset_y, largura_celula, altura_celula, selecionando):
    x, y = pos
    coluna = (x - offset_x) // largura_celula
    linha = (y - offset_y) // altura_celula

    if 0 <= linha < len(grade) and 0 <= coluna < len(grade[0]):
        if (linha, coluna) not in selecionando:
            selecionando.append((linha, coluna))