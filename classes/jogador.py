from colorama import Fore, Style

class Jogador:
    
    def __init__(self, nome):
        self.nome = nome
        self.periodo = 1
        self.reprovacoes = 0
        self.disciplinas_pendentes = []
    
    def passou_de_periodo(self):
        self.periodo += 1

    def adicionar_pendencia(self, disciplina):

        if disciplina not in self.disciplinas_pendentes:
            self.disciplinas_pendentes.append(disciplina)
    
    def mostrar_pendencias(self):

        if len(self.disciplinas_pendentes) == 0:
            print(Fore.GREEN + "🎉 Sem pendências." + Style.RESET_ALL)
            return
        print("="*50)
        print(Fore.LIGHTYELLOW_EX + "Pendências:" + Style.RESET_ALL)

        for disciplina in self.disciplinas_pendentes:
            print(f"{disciplina.nome}")