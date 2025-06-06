class Carro:
    def __init__(self, marca, modelo):
        # Atributos para armazenar marca e modelo do carro
        self.marca = marca
        self.modelo = modelo
        # A velocidade inicial do carro começa em 0
        self.velocidade_atual = 0

    def acelerar(self):
        # Método para aumentar a velocidade em 10 unidades
        self.velocidade_atual += 10

    def frear(self):
        # Método para diminuir a velocidade em 10 unidades, sem ficar negativa
        if self.velocidade_atual >= 10:
            self.velocidade_atual -= 10
        else:
            self.velocidade_atual = 0

    def exibir_velocidade(self):
        # Método para mostrar a velocidade atual do carro
        print(f"Velocidade atual: {self.velocidade_atual} km/h")


# Exemplo de uso
meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_velocidade()  # Deve mostrar 0 km/h
meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.exibir_velocidade()  # Deve mostrar 20 km/h
meu_carro.frear()
meu_carro.exibir_velocidade()  # Deve mostrar 10 km/h
