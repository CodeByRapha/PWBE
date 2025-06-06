class Funcionario:
    def __init__(self, nome_funcionario, salario, cargo_funcionario):
        self.nome_funcionario = nome_funcionario
        self.salario = salario
        self.cargo_funcionario = cargo_funcionario
        self.imposto = 64          # Valor fixo do imposto
        self.beneficio = 78        # Valor fixo do benefício

    def descontos_aplicados(self):
        # Calcula o salário líquido considerando imposto e benefício
        salario_liquido = self.salario - self.imposto + self.beneficio

        print(f"Nome: {self.nome_funcionario}")
        print(f"Cargo: {self.cargo_funcionario}")
        print(f"Salário Bruto: R${self.salario:.2f}")
        print(f"Imposto: R${self.imposto:.2f}")
        print(f"Benefício: R${self.beneficio:.2f}")
        print(f"Salário Líquido: R${salario_liquido:.2f}")


funcionario = Funcionario("Raphaela Tavares", 3000, "Gestor de TI")
funcionario.descontos_aplicados()
