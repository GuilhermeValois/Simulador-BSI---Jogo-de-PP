from colorama import Fore, Style

class Pergunta:
    def __init__(self, enunciado, categoria, alternativas, resposta):
        self.enunciado = enunciado
        self.categoria = categoria
        self.alternativas = alternativas
        self.resposta = resposta

    def verificar_resposta(self, resposta_usuario):
        if resposta_usuario.upper() == self.resposta:
            print(Fore.GREEN + "\n✅ Resposta correta\n" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "\n❌ Resposta incorreta.\n" + Style.RESET_ALL)
            return False
    
    def mostrar_pergunta(self):
        print("="*50)
        print(Fore.CYAN + f"Categoria: {self.categoria.upper()}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Pergunta: {self.enunciado}\n" + Style.RESET_ALL)
        print("="*50)
        for letra, texto in self.alternativas.items():
            print(f"{letra} - {texto}")
        print("="*50)

    
