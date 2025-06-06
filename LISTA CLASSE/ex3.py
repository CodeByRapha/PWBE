class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        # Calcula a área do retângulo
        return self.largura * self.altura

    def calcular_perimetro(self):
        # Calcula o perímetro do retângulo
        return 2 * (self.largura + self.altura)

calcular_Retangulo = Retangulo(5, 10)

print(f"A área do retângulo é: {calcular_Retangulo.calcular_area()}")
print(f"O perímetro do retângulo é: {calcular_Retangulo.calcular_perimetro()}")
