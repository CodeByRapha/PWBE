import random

# Função para deixar a carta no formato "número (cor)"
def formatar_carta(carta):
    numero, cor = carta.split('_')
    return f'{numero} ({cor})'

class JogoCartas:
    def __init__(self, num_jogadores):
        self.num_jogadores = num_jogadores
        self.baralho = self.criar_baralho()  # Cria o baralho padrão do jogo
        # Dicionário para armazenar as cartas de cada jogador: chave = número do jogador, valor = lista de cartas
        self.maos = {i: [] for i in range(1, num_jogadores+1)}
        self.mesa = []  # Lista para armazenar as cartas jogadas na mesa

    def criar_baralho(self):
        cores = ['vermelho', 'verde', 'azul', 'amarelo']
        cartas = []
        # Gera cartas numeradas de 0 a 9 para cada cor
        for cor in cores:
            for numero in range(10):
                cartas.append(f'{numero}_{cor}')
        return cartas

    def embaralhar(self):
        # Embaralha o baralho usando shuffle do random
        random.shuffle(self.baralho)

    def distribuir(self, qtd_cartas=7):
        # Distribui uma quantidade fixa de cartas para cada jogador
        for _ in range(qtd_cartas):
            for jogador in self.maos:
                if self.baralho:
                    carta = self.baralho.pop()  # Remove carta do topo do baralho
                    self.maos[jogador].append(carta)  # Adiciona à mão do jogador

    def jogar_carta(self, jogador, carta):
        # Tenta jogar a carta do jogador para a mesa
        if carta in self.maos[jogador]:
            self.maos[jogador].remove(carta)  # Remove da mão do jogador
            self.mesa.append(carta)  # Adiciona à mesa
            print(f'\nJogador {jogador} jogou {formatar_carta(carta)}')
            return True
        else:
            print(f'\nJogador {jogador} não tem a carta {formatar_carta(carta)}')
            return False

    def mostrar_mao(self, jogador):
        # Retorna as cartas que o jogador possui
        return self.maos[jogador]

    def mostrar_mesa(self):
        # Retorna a lista de cartas jogadas na mesa
        return self.mesa


# Exemplo de uso do jogo:
jogo = JogoCartas(num_jogadores=3)
jogo.embaralhar()  # Embaralha as cartas
jogo.distribuir()  # Distribui 7 cartas para cada jogador

print("\n--- Mãos dos Jogadores ---")
for i in range(1, 4):
    cartas_formatadas = [formatar_carta(c) for c in jogo.mostrar_mao(i)]
    print(f'Jogador {i}: {", ".join(cartas_formatadas)}')

# Jogador 1 joga a primeira carta da sua mão
carta_para_jogar = jogo.mostrar_mao(1)[0]
jogo.jogar_carta(1, carta_para_jogar)

print("\n--- Cartas na Mesa ---")
cartas_na_mesa = [formatar_carta(c) for c in jogo.mostrar_mesa()]
print(", ".join(cartas_na_mesa))
