class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []  # Lista para armazenar as consultas

    def adicionar_consulta(self, consulta):
        self.historico.append(consulta)  # Adiciona nova consulta

    def exibir_consultas(self):
        print(f"Consultas da paciente {self.nome}:")
        for c in self.historico:  # Mostra uma consulta por linha
            print("-", c)


# Exemplo de uso:
paciente = Paciente("Raphaela Tavares", 40)
paciente.adicionar_consulta("Consulta de rotina - 10/05/2025")
paciente.adicionar_consulta("Retorno - 24/05/2025")

paciente.exibir_consultas()
