class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo            
        self.autor = autor              
        self.paginas = paginas         
        self.disponivel = True          # status do livro: disponível ou não

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False     # marca como emprestado
            return True
        return False                   # já está emprestado

    def devolver(self):
        self.disponivel = True         # marca como disponível

    def esta_disponivel(self):
        return self.disponivel         # retorna se o livro está disponível


# cria um livro
livro1 = Livro("Os Sete Maridos de Evelyn Hugo", "Taylor Jenkins Reid", 400)

# tenta emprestar e imprime o status
if livro1.emprestar():
    status = "emprestado"
else:
    status = "não disponível"

print(f"Livro '{livro1.titulo}': {status}")

# devolve o livro e imprime o status
livro1.devolver()
print(f"Livro '{livro1.titulo}': devolvido e disponível")
