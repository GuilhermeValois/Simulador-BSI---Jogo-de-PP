import utils
from jogador import Jogador
from disciplina import Disciplina
from pergunta import Pergunta
import pygame
import sys


def jogar(jogador, lista_disciplinas, perguntas_por_categoria):
    reprovacao = 0
    while jogador.periodo <= 9:
        if reprovacao == 3:
            print("Reprovado")
            return
        acertos = 0
        disciplinas = utils.discplina_por_periodo(lista_disciplinas, jogador.periodo)
        if len(jogador.disciplinas_pendentes) > 0 and jogador.periodo <= 8:
            jogador.mostrar_pendencias()
            while True:
                jogador.mostrar_pendencias()
                pagar = input("Deseja pagar pendências?").strip().lower()
                if pagar == 's':
                    disciplinas.append(jogador.disciplinas_pendentes)
                    break
                elif pagar == 'n':
                    break
                print("Opção inválida")
        elif len(jogador.disciplinas_pendentes) > 0 and jogador.periodo == 9:
            disciplinas.extend(jogador.disciplinas_pendentes)

        for disciplina in disciplinas:
            pergunta = disciplina.sortear_pergunta_da_disciplina(perguntas_por_categoria)
            pergunta.perguntar()
            resposta_do_usuario = input("").strip().upper()
            acertou = pergunta.verificar_resposta(resposta_do_usuario, disciplina,jogador)
            if acertou == True:
                acertos += 1
        if acertos >= len(disciplinas)/2:
            jogador.periodo += 1
            print("Aprovado")
        else:
            reprovacao += 1
            print("Reprovado")
