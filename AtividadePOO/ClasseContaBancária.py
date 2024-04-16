class ContaBancaria:
    def __init__(self, numero, titular, saldo=0, limite=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.conta_ativa = False

    def sacar(self, valor):
        if self.conta_ativa and valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        if self.conta_ativa:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Conta bloqueada, não é possível realizar depósito.")

    def bloquear(self):
        self.conta_ativa = False
        print("Conta bloqueada.")

    def desbloquear(self):
        self.conta_ativa = True
        print("Conta desbloqueada.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def mudar_limite(self, novo_limite):
        if self.conta_ativa:
            self.limite = novo_limite
            print(f"Limite alterado para R${novo_limite:.2f}.")
        else:
            print("Conta bloqueada, não é possível alterar o limite.")

conta = ContaBancaria(numero="954628", titular="Fabianny Mendes", saldo=1000, limite=500)
conta.verificar_saldo()
conta.sacar(20)
conta.depositar(30)
conta.sacar(40)
conta.verificar_saldo()
conta.bloquear()
conta.depositar(50)
conta.desbloquear()
conta.mudar_limite(100)
