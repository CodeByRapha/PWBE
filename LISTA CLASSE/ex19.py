import random

class JogoAdivinhacao:
    def __init__(self, minimo=1, maximo=100):
         # Gera um número aleatório no início do jogo
        self.numero_secreto = random.randint(minimo, maximo)

    def tentar_palpite(self, palpite):
        # Verifica o palpite e retorna dica
        if palpite == self.numero_secreto:
            return "Acertou!"
        elif palpite < self.numero_secreto:
            return "Maior"
        else:
            return "Menor"

jogo = JogoAdivinhacao() # inicia o jogo com número secreto entre 1 e 100

while True:
    palpite = int(input("Digite seu palpite: ")) # jogador digita um número
    resultado = jogo.tentar_palpite(palpite)    # Verifica o palpite
    print(resultado)    # mostra dica
    if resultado == "Acertou!":
        break   # Fim do jogo quando o palpite é acertado