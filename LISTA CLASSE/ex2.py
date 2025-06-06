class ContaBancaria:
    
    def __init__(self, numero_conta, nome_titular, saldo=0):
        # inicializa os atributos da conta bancária
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        # verifica se o valor é positivo antes de adicionar ao saldo
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!!")
        else:
            print("Para depositar, o valor tem que ser positivo")

    def sacar(self, valor):
        # verifica se o valor é válido e se há saldo suficiente para saque
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque no valor de {valor:.2f} efetuado com sucesso! ")
        elif valor > self.saldo:
            print("Valor não é suficiente para saque")
        else:
            print("O valor tem que ser positivo.")

    def exibir_saldo(self):
        # mostra o saldo atual da conta
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")

# criação de uma conta com saldo inicial
conta_Banco = ContaBancaria(4444, "Raphaela Tavares", 10000)

# operações na conta
conta_Banco.exibir_saldo()
conta_Banco.depositar(500)
conta_Banco.exibir_saldo()
conta_Banco.sacar(300)
conta_Banco.exibir_saldo()
conta_Banco.sacar(1500)
