class Pergunta:
    def __init__(self, enunciado, categoria, alternativas, resposta):
        self.enunciado = enunciado
        self.categoria = categoria
        self.alternativas = alternativas
        self.resposta = resposta

    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.lower().strip() == self.resposta.lower().strip()