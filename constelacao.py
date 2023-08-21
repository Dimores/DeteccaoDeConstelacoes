from estrela import Estrela

class Constelacao:
    def __init__(self, nome):
        self.nome = nome
        self.estrelas = []

    def adicionar_estrela(self, estrela):
        self.estrelas.append(estrela)

    def imprimir_estrelas(self):
        print(f"Estrelas na constelação {self.nome}:")
        for estrela in self.estrelas:
            print(estrela.informacoes())
            print("-" * 20)

# Criando algumas estrelas
estrela1 = Estrela("Estrela 1", "A5V", 2.5)
estrela2 = Estrela("Estrela 2", "G0V", 3.8)
estrela3 = Estrela("Estrela 3", "B2IV", 1.2)

# Criando uma constelação e adicionando estrelas
constelacao = Constelacao("Orion")
constelacao.adicionar_estrela(estrela1)
constelacao.adicionar_estrela(estrela2)
constelacao.adicionar_estrela(estrela3)

# Imprimindo informações das estrelas na constelação
constelacao.imprimir_estrelas()
