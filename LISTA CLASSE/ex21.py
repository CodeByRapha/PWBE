class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []  # lista de pedidos passados

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []  # lista de (produto, quantidade)
        self.status = 'aberto'  # aberto, fechado

    def adicionar_item(self, produto, quantidade=1):
        self.itens.append((produto, quantidade))

    def calcular_total(self, desconto=0, frete=0):
        subtotal = sum(p.preco * q for p, q in self.itens)
        total = subtotal * (1 - desconto) + frete
        return total

    def fechar_pedido(self):
        self.status = 'fechado'
        self.cliente.historico.append(self)

def recomendar_produtos(cliente, todos_produtos):
    # recomenda produtos que o cliente não comprou ainda (simples)
    comprados = {p.id for pedido in cliente.historico for p, _ in pedido.itens}
    return [p for p in todos_produtos if p.id not in comprados]

# Exemplo uso
p1 = Produto(1, "Caneca", 20)
p2 = Produto(2, "Camiseta", 50)
cliente = Cliente("Raphaela")
pedido = Pedido(cliente)
pedido.adicionar_item(p1, 2)
pedido.adicionar_item(p2)
print("Total com desconto e frete:", pedido.calcular_total(desconto=0.1, frete=10))
pedido.fechar_pedido()

print("Recomendações:", [p.nome for p in recomendar_produtos(cliente, [p1,p2])])
