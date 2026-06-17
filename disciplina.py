import random

class Disciplina:
    
    def __init__(self,nome, periodo, categoria):
        
        self.nome = nome
        self.periodo = periodo
        self.categoria = categoria

    def sortear_pergunta_da_disciplina(self,  perguntas_por_categoria):
        
        perguntas = perguntas_por_categoria[self.categoria]
        print(f"{self.nome}\n")
        return random.choice(perguntas)
