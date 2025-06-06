class Produto:
    def __init__(self, nome, preco):
        self.nome = nome      # nome do produto
        self.preco = preco    # preço unitário

class LojaVirtual:
    def __init__(self):
        self.produtos = []   # lista de produtos disponíveis
        self.carrinho = []   # lista de produtos no carrinho

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)  # adiciona produto na loja

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.append(produto)  # adiciona produto ao carrinho

    def aplicar_desconto(self, percentual):
        for produto in self.carrinho:
            produto.preco *= (1 - percentual / 100)  # aplica desconto % no preço

    def calcular_total(self):
        return sum(produto.preco for produto in self.carrinho)  # soma total do carrinho

# ex simples de uso

loja = LojaVirtual()

p1 = Produto("Camisa", 50)
p2 = Produto("Calça", 120)

loja.cadastrar_produto(p1)
loja.cadastrar_produto(p2)

loja.adicionar_ao_carrinho(p1)
loja.adicionar_ao_carrinho(p2)

print(f"Total sem desconto: R${loja.calcular_total():.2f}")
loja.aplicar_desconto(10)  # 10% de desconto
print(f"Total com desconto: R${loja.calcular_total():.2f}")
