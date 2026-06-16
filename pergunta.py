
class Pergunta:
    def __init__(self, enunciado, categoria, alternativas, resposta):
        self.enunciado = enunciado
        self.categoria = categoria
        self.alternativas = alternativas
        self.resposta = resposta

    def verificar_resposta(self, resposta_usuario, disciplina,jogador):
        
        if resposta_usuario == self.resposta:
            print("Resposta correta")
            return True
        else:
            jogador.adicionar_pendencias(disciplina)
            return False
    
    def perguntar(self):
        print(f"{self.enunciado}\n")
        print(f"A-{self.alternativas['A']}")
        print(f"B-{self.alternativas['B']}")
        print(f"C-{self.alternativas['C']}")
        print(f"D-{self.alternativas['D']}")

    
