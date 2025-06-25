class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Fornecedor:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, categoria, fornecedor, preco_compra, preco_venda, quantidade=0):
        self.nome = nome
        self.categoria = categoria
        self.fornecedor = fornecedor
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade

    def comprar(self, qtd):
        self.quantidade += qtd

    def vender(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            return True
        return False

    def __str__(self):
        return f"{self.nome} - Qtd: {self.quantidade} - Venda: R${self.preco_venda}"

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def relatorio(self):
        print("Relatório de Estoque:")
        for p in self.produtos:
            print(p)

# Exemplo uso
cat1 = Categoria("Eletrônicos")
forn1 = Fornecedor("Fornecedor Raphaela")
prod = Produto("Fone de ouvido", cat1, forn1, 50, 80, 10)

estoque = Estoque()
estoque.adicionar_produto(prod)
prod.comprar(5)  # compra 5 unidades
prod.vender(3)   # vende 3 unidades

estoque.relatorio()
