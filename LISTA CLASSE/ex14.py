class MaquinaDeVendas:
    def __init__(self):
        self.estoque = {}  # produto: [preço, quantidade]
        self.produto = None  # produto selecionado
        self.dinheiro = 0    # dinheiro inserido

    def cadastrar_produto(self, nome, preco, qtd):
        # adiciona produto ou atualiza quantidade
        if nome in self.estoque:
            self.estoque[nome][1] += qtd
        else:
            self.estoque[nome] = [preco, qtd]

    def selecionar_produto(self, nome):
        # seleciona produto se disponível
        if nome in self.estoque and self.estoque[nome][1] > 0:
            self.produto = nome
            print(f'Produto "{nome}" selecionado.')
        else:
            print("Produto indisponível")

    def inserir_dinheiro(self, valor):
        # adiciona dinheiro para compra
        if valor > 0:
            self.dinheiro += valor
            print(f'Dinheiro inserido: R${valor:.2f}')
        else:
            print("Valor inválido")

    def finalizar_compra(self):
        # finaliza compra se dinheiro e produto válidos
        if not self.produto:
            print("Nenhum produto selecionado")
            return
        preco, qtd = self.estoque[self.produto]
        if self.dinheiro < preco:
            falta = preco - self.dinheiro
            print(f"Dinheiro insuficiente. Faltam R${falta:.2f}")
            return
        self.estoque[self.produto][1] -= 1  # reduz estoque
        troco = self.dinheiro - preco
        print(f"Compra realizada: {self.produto}")
        if troco > 0:
            print(f"Troco retornado: R${troco:.2f}")
        self.produto = None
        self.dinheiro = 0

    def mostrar_estoque(self):
        # exibe produtos com preço e quantidade
        print("Estoque disponível:")
        for p, (preco, qtd) in self.estoque.items():
            print(f"{p}: R${preco:.2f} - {qtd} unidades")
        print()  # linha em branco para melhor leitura

# exemplo de uso da máquina de vendas
if __name__ == "__main__":
    maquina = MaquinaDeVendas()
    maquina.cadastrar_produto("Refrigerante", 5.00, 10)
    maquina.cadastrar_produto("Chips", 3.50, 5)
    maquina.mostrar_estoque()
    maquina.selecionar_produto("Refrigerante")
    maquina.inserir_dinheiro(10)
    maquina.finalizar_compra()
    maquina.mostrar_estoque()
