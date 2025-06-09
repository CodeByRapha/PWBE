class Biblioteca:
    def __init__(self):
        # armazena os livros cadastrados
        self.livros = {}

    def cadastrar_livro(self, titulo):
        # cadastra um novo livro se ele ainda não estiver na biblioteca
        if titulo not in self.livros:
            self.livros[titulo] = {
                'disponivel': True,
                'emprestado_para': None
            }

    def emprestar_livro(self, titulo, usuario):
        # faz o empréstimo se o livro existir e estiver disponível
        if titulo in self.livros and self.livros[titulo]['disponivel']:
            self.livros[titulo]['disponivel'] = False
            self.livros[titulo]['emprestado_para'] = usuario
            print(f'Livro "{titulo}" emprestado para {usuario}.')
        else:
            print(f'Livro "{titulo}" não está disponível para empréstimo.')

    def devolver_livro(self, titulo):
        # devolve o livro se ele existir e estiver emprestado
        if titulo in self.livros and not self.livros[titulo]['disponivel']:
            self.livros[titulo]['disponivel'] = True
            self.livros[titulo]['emprestado_para'] = None
            print(f'Livro "{titulo}" foi devolvido.')
        else:
            print(f'Livro "{titulo}" não está emprestado.')

    def verificar_disponibilidade(self, titulo):
        # Retorna True se o livro estiver disponível
        if titulo in self.livros:
            return self.livros[titulo]['disponivel']
        return False

# criando a biblioteca
biblioteca = Biblioteca()

# Cadastrando livros
biblioteca.cadastrar_livro('Os Sete Maridos de Evelyn Hugo')
biblioteca.cadastrar_livro('É assim que acaba')

# emprestando livro
biblioteca.emprestar_livro('Os Sete Maridos de Evelyn Hugo', 'Raphaela')

# verificando disponibilidade
print('Os Sete Maridos de Evelyn Hugo está disponível?', biblioteca.verificar_disponibilidade('Os Sete Maridos de Evelyn Hugo'))
print('É assim que acaba está disponível?', biblioteca.verificar_disponibilidade('É assim que acaba'))

# devolvendo livro
biblioteca.devolver_livro('Os Sete Maridos de Evelyn Hugo')

# verificando de novo
print('Os Sete Maridos de Evelyn Hugo está disponível agora?', biblioteca.verificar_disponibilidade('Os Sete Maridos de Evelyn Hugo'))
