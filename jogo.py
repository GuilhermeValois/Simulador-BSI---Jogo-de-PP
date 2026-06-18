import utils
from jogador import Jogador
from disciplina import Disciplina
from pergunta import Pergunta
from colorama import Fore, Style
import os


def jogar(jogador, lista_disciplinas, perguntas_por_categoria, perguntas_tcc):
    reprovacao = 0
    while jogador.periodo <= 8:
        if reprovacao == 3:
            print(Fore.RED + "❌ jubilado" + Style.RESET_ALL)
            return
        acertos = 0
        disciplinas = utils.disciplina_por_periodo(lista_disciplinas, jogador.periodo, jogador.nome)
        if len(jogador.disciplinas_pendentes) > 0 and jogador.periodo <= 8:
            jogador.mostrar_pendencias()
            while True:
                pagar = input(Fore.CYAN + "Deseja pagar pendências? " + Style.RESET_ALL).strip().lower()
                if pagar == 's':
                    disciplinas.extend(jogador.disciplinas_pendentes)
                    jogador.disciplinas_pendentes = []
                    break
                elif pagar == 'n':
                    break
                print(Fore.YELLOW + "⚠️ Opção inválida" + Style.RESET_ALL)
        
        disciplinas_que_reprovou = []
        for disciplina in disciplinas:
            pergunta = disciplina.sortear_pergunta_da_disciplina(perguntas_por_categoria)
            pergunta.mostrar_pergunta(disciplina.nome)
            resposta_do_usuario = input(Fore.LIGHTYELLOW_EX + "📝 Sua resposta: " + Style.RESET_ALL).strip().upper()
            while resposta_do_usuario not in ['A','B','C','D']:
                print(Fore.RED + "❌ RESPOSTA INVÁLIDA" + Style.RESET_ALL)
                resposta_do_usuario = input(Fore.LIGHTYELLOW_EX + "📝 Sua resposta: " + Style.RESET_ALL).strip().upper()
            acertou = pergunta.verificar_resposta(resposta_do_usuario)
            if acertou == True:
                acertos += 1
            else:
                disciplinas_que_reprovou.append(disciplina)
        if acertos >= len(disciplinas)/2 and jogador.periodo:
            jogador.disciplinas_pendentes.extend(disciplinas_que_reprovou)
            jogador.periodo += 1
            print(Fore.GREEN + "✅ Aprovado" + Style.RESET_ALL)
        else:
            reprovacao += 1
            print(Fore.RED + "❌ Reprovado, você pagará novamente esse período" + Style.RESET_ALL)

    if jogador.periodo == 9:
        while True:
            disciplinas_que_reprovou = []
            if len(jogador.disciplinas_pendentes) > 0: 
                print(Fore.LIGHTYELLOW_EX + "⚠️ Você tem que pagar as pendências antes do TCC" + Style.RESET_ALL)
                jogador.mostrar_pendencias()
                for disciplina in jogador.disciplinas_pendentes:
                    pergunta = disciplina.sortear_pergunta_da_disciplina(perguntas_por_categoria)
                    pergunta.mostrar_pergunta()
                    resposta_do_usuario = input(Fore.LIGHTYELLOW_EX + "📝 Sua resposta: " + Style.RESET_ALL).strip().upper()
                    while resposta_do_usuario not in ['A','B','C','D']:
                        print(Fore.RED + "❌ RESPOSTA INVÁLIDA" + Style.RESET_ALL)
                        resposta_do_usuario = input(Fore.LIGHTYELLOW_EX + "📝 Sua resposta: " + Style.RESET_ALL).strip().upper()
                    acertou = pergunta.verificar_resposta(resposta_do_usuario, disciplina,jogador)
                    if acertou == False:
                        disciplinas_que_reprovou.append(disciplina)
                jogador.disciplinas_pendentes = disciplinas_que_reprovou
                if 0 == len(jogador.disciplinas_pendentes):
                    print(Fore.GREEN + "✅ Aprovado, pode fazer tcc" + Style.RESET_ALL)
                    aprovacao = utils.fazer_tcc(perguntas_tcc)
                    if aprovacao == True:
                        print(Fore.GREEN + "🎉 Você se formou em BSI! Parabéns!" + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.RED + "😔 Seu TCC não foi aprovado! Tente de novo" + Style.RESET_ALL)
                        continue
                else:
                    reprovacao += 1
                    if reprovacao == 3:
                        print(Fore.RED + "❌ jubilado" + Style.RESET_ALL)
                        return
                    else:
                        print(Fore.RED + "❌ Reprovado, pagará novamente as pendências que falta" + Style.RESET_ALL)
            else:
                print("Agora é a hora de fazer o TCC")
                aprovacao = utils.fazer_tcc(perguntas_tcc)
                if aprovacao == True:
                    print(Fore.GREEN + "🎉 Você se formou em BSI! Parabéns!" + Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + "😔 Seu TCC não foi aprovado! Tente de novo" + Style.RESET_ALL)
                    continue