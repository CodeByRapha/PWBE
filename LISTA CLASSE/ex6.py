class Produto():
    def __init__(self, nome, preco, qtd_estoque):
        self.nome = nome              # Nome do produto
        self.preco = preco            # Preço unitário do produto
        self.qtd_estoque = qtd_estoque # Quantidade disponível no estoque
    
    def valor_estoque(self):
        return self.preco * self.qtd_estoque  # Calcula valor total do estoque
    
    def verificar_disponibilidade(self):
        print(f"Nome produto: {self.nome}\nPreço produto: {self.preco}\nProdutos disponiveis: {self.qtd_estoque} ")
        return self.qtd_estoque > 0  # Retorna True se houver produtos no estoque, senão False
        
produto = Produto("Livro", 50.00, 10)
print(f"Valor total em estoque: R$ {produto.valor_estoque():.2f}")
if produto.verificar_disponibilidade():
    print("O produto está disponível.")
else:
    print("O produto não está disponível.")
