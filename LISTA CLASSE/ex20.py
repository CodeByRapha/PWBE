class Peca:
    def __init__(self, simbolo, cor):
        self.simbolo = simbolo  # ex: ♙, ♜, ♚
        self.cor = cor          # branco ou preto

    def __str__(self):
        # Retorna o símbolo da peça para exibição
        return self.simbolo

class JogoXadrez:
    def __init__(self):
         # cria um tabuleiro vazio (8x8 com None)
        self.tabuleiro = [[None]*8 for _ in range(8)]
        self.iniciar() # posiciona as peças iniciais

    def iniciar(self):
        # Peças pretas
        self.tabuleiro[0] = [Peca('♜', 'preto'), None, None, None, Peca('♚', 'preto'), None, None, Peca('♜', 'preto')]
        self.tabuleiro[1] = [Peca('♟', 'preto') for _ in range(8)]

        # peças brancas
        self.tabuleiro[6] = [Peca('♙', 'branco') for _ in range(8)]
        self.tabuleiro[7] = [Peca('♖', 'branco'), None, None, None, Peca('♔', 'branco'), None, None, Peca('♖', 'branco')]

    def mostrar_tabuleiro(self):
        letras = "a b c d e f g h".split()
        for i in range(8):
            linha = self.tabuleiro[i]
            print(f"{8 - i} |", end=" ")
            for p in linha:
                # mostra símbolo da peça ou "__" se vazio
                print(p if p else "__", end=" ")
            print()
        print("   ", " ".join(letras)) # letras das colunas

jogo = JogoXadrez()
jogo.mostrar_tabuleiro()

