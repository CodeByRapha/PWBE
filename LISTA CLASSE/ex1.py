import math

class Circulo:
    def __init__(self, raio):
        # inicializa o raio do círculo
        self.raio = raio

    def calcular_area(self):
        # calcula a área do círculo usando a fórmula π * r²
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
        # calcula o perímetro (circunferência) usando a fórmula 2 * π * r
        return 2 * math.pi * self.raio

# cria um objeto da classe Circulo com raio 8
calcular_Circulo = Circulo(8)

# exibe a área e o perímetro do círculo
print(f"Área: {calcular_Circulo.calcular_area():.2f} ")
print(f"Perímetro: {calcular_Circulo.calcular_perimetro():.2f}")
