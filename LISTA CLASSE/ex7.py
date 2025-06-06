import math  # importa o módulo math

class Triangulo():
    # método construtor que inicializa os lados, base e altura do triângulo
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    # método para verificar se os lados formam um triângulo válido
    def verificar(self):
        if (self.lado1 + self.lado2 > self.lado3) and (self.lado2 + self.lado3 > self.lado2) and (self.lado1 + self.lado3 > self.lado2):
            print("Triângulo perfeito")
        else:
            print("Triângulo não é perfeito")

    # método para calcular a área do triângulo usando base e altura
    def calcular_area(self):
        self.area = self.base * self.altura / 2
        print(f"A área do triângulo é {self.area}")

triangulo = Triangulo(1, 2, 3, 15, 10) #criando um objeto da classe Triangulo com valores para lados, base e altura
triangulo.verificar() # chama o método para verificar se os lados formam um triângulo válido
triangulo.calcular_area() # chama o método para calcular e mostrar a área do triângulo