class Estrela:
    def __init__(self, nome, tipo_espectral, magnitude):
        self.nome = nome
        self.tipo_espectral = tipo_espectral
        self.magnitude = magnitude

    def brilhar(self):
        return f"A estrela {self.nome} está brilhando intensamente."

    def informacoes(self):
        return f"Nome: {self.nome}\nTipo Espectral: {self.tipo_espectral}\nMagnitude: {self.magnitude}"

# Criando uma instância da classe Estrela
sol = Estrela("Sol", "G2V", -26.74)

# Acessando métodos e atributos da instância
print(sol.brilhar())
print(sol.informacoes())
