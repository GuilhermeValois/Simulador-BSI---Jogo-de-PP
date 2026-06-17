import colorama

class Pergunta:
    def __init__(self, enunciado, categoria, alternativas, resposta):
        self.enunciado = enunciado
        self.categoria = categoria
        self.alternativas = alternativas
        self.resposta = resposta

    def verificar_resposta(self, resposta_usuario):
        
        if resposta_usuario == self.resposta:
            print("\n✅Resposta correta\n")
            return True
        else:
            print()
            return False
    
    def mostrar_pergunta(self):
        print(f"{self.enunciado}\n")
        print(f"A-{self.alternativas['A']}")
        print(f"B-{self.alternativas['B']}")
        print(f"C-{self.alternativas['C']}")
        print(f"D-{self.alternativas['D']}")

    
