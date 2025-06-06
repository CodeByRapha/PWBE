class Cliente:
    def __init__(self, nome):
        self.nome = nome  # nome do cliente

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero      # número da conta
        self.cliente = cliente    # cliente dono da conta
        self.saldo = 0           # saldo inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor  # adiciona ao saldo

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor  # remove do saldo
            return True
        return False

class Banco:
    def __init__(self):
        self.clientes = []   # lista de clientes
        self.contas = []     # lista de contas

    def cadastrar_cliente(self, nome):
        cliente = Cliente(nome)
        self.clientes.append(cliente)
        return cliente

    def abrir_conta(self, cliente, numero):
        conta = Conta(numero, cliente)
        self.contas.append(conta)
        return conta

    def depositar(self, conta, valor):
        conta.depositar(valor)

    def sacar(self, conta, valor):
        return conta.sacar(valor)

    def transferir(self, conta_origem, conta_destino, valor):
        if conta_origem.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False

# exemplo de uso
banco = Banco()

# cadastro clientes
cliente1 = banco.cadastrar_cliente("Maria")
cliente2 = banco.cadastrar_cliente("João")

# abrir contas
conta1 = banco.abrir_conta(cliente1, 101)
conta2 = banco.abrir_conta(cliente2, 102)

# operações
banco.depositar(conta1, 1000)
print(f"Saldo conta1: R${conta1.saldo}")
banco.sacar(conta1, 200)
print(f"Saldo conta1 após saque: R${conta1.saldo}")

if banco.transferir(conta1, conta2, 300):
    print("Transferência realizada com sucesso!")
else:
    print("Falha na transferência.")

print(f"Saldo conta1: R${conta1.saldo}")
print(f"Saldo conta2: R${conta2.saldo}")
