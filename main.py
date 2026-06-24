import sistema.utils as utils
from classes.jogador import Jogador
import sistema.jogo as jogo
import pygame
from interface import constantes
from interface import popup

lista_disciplinas = utils.carregar_disciplinas()
lista_perguntas = utils.carregar_perguntas()
perguntas_tcc = utils.carregar_tcc()

perguntas_por_categoria = {
    'programacao': [],
    'matematica_logica': [],
    'dados': [],
    'infraestrutura': [],
    'sistemas_informacao': [],
    'gestao': []
}

for pergunta in lista_perguntas:
    perguntas_por_categoria[pergunta.categoria].append(pergunta)

tela = pygame.display.set_mode((constantes.LARGURA,constantes.ALTURA))
jogo.jogar_com_interface(tela,perguntas_por_categoria,perguntas_tcc,lista_disciplinas)
'''
nome = utils.nome_jogador()
jogador = Jogador(nome)

jogo.jogar(jogador, lista_disciplinas, perguntas_por_categoria, perguntas_tcc)
'''
