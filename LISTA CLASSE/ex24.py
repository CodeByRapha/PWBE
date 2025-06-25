class Animal:
    def __init__(self, nome, especie, dieta):
        self.nome = nome
        self.especie = especie
        self.dieta = dieta  # exxx: 'carnívoro', 'herbívoro'

class Habitat:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo  # ex: 'selva', 'aquático'
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

class Veterinario:
    def __init__(self, nome):
        self.nome = nome

    def cuidar(self, animal):
        print(f"Veterinária {self.nome} cuidando do {animal.nome}")

class Funcionario:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

# saída
hab1 = Habitat("Selva 1", "selva")
a1 = Animal("Leão", "Felino", "carnívoro")
hab1.adicionar_animal(a1)

vet = Veterinario("Dra. Raphaela")
vet.cuidar(a1)
