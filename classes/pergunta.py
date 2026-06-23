from colorama import Fore, Style

class Pergunta:
    def __init__(self, enunciado, categoria, alternativas, resposta):
        self.enunciado = enunciado
        self.categoria = categoria
        self.alternativas = alternativas
        self.resposta = resposta

    def verificar_resposta(self, resposta_usuario):
        if resposta_usuario.upper() == self.resposta:
            print(Fore.GREEN + "\n✅ Resposta correta" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "\n❌ Resposta incorreta." + Style.RESET_ALL)
            return False
    
    def mostrar_pergunta(self, disciplina_nome=None):
        print("="*50)
        if disciplina_nome:
            print(Fore.CYAN + f"Disciplina: {disciplina_nome}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Categoria: {self.categoria.upper()}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Pergunta: {self.enunciado}" + Style.RESET_ALL)
        print("-"*50)
        for letra, texto in self.alternativas.items():
            print(Fore.GREEN + f"{letra} - {texto}" + Style.RESET_ALL)
        print("="*50)

    
