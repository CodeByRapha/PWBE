class Agenda:
    def __init__(self):
        self.contatos = {}  # dicionário para armazenar contatos

    def adicionar(self, nome, telefone):
        self.contatos[nome] = telefone  # adiciona novo contato

    def editar(self, nome, novo_telefone):
        if nome in self.contatos:
            self.contatos[nome] = novo_telefone  # atualiza telefone do contato

    def remover(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]  # remove contato da agenda

    def buscar(self, termo):
        # retorna contatos que contenham o termo no nome ou telefone
        return {nome: tel for nome, tel in self.contatos.items() if termo in nome or termo in tel}

# exemplo de uso
agenda = Agenda()
agenda.adicionar("Raphaela", "1234-5678")
agenda.adicionar("Carlos", "8765-4321")

print(agenda.buscar("Rapha"))  # busca por nome
agenda.editar("Raphaela", "1111-2222")
agenda.remover("Carlos")

print(agenda.contatos)  # exibe contatos restantes
