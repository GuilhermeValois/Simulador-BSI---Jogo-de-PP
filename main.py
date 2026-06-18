import utils
from jogador import Jogador
import jogo

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

nome = utils.nome_jogador()
jogador = Jogador(nome)

jogo.jogar(jogador, lista_disciplinas, perguntas_por_categoria, perguntas_tcc)

