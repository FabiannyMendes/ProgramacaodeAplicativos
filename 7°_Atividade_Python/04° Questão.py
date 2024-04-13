#4- Crie uma classe para implementar uma conta corrente.
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
#Os métodos são os seguintes: alterarNome, depósito e saque;
#No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.


class ContaCorrente:
  def _init_(self, numero_conta, nome_correntista, saldo=0):
    self.numero_conta = numero_conta
    self.nome_correntista = nome_correntista
    self.saldo = saldo

  def alterar_nome(self, novo_nome):
    self.nome_correntista = novo_nome

  def deposito(self, valor):
    self.saldo += valor

  def saque(self, valor):
    if valor <= self.saldo:
      self.saldo -= valor
    else:
      print("Saldo insuficiente")

conta = ContaCorrente(12345, "Kleber")

conta.deposito(7000)

conta.saque(67)

print(f"Saldo: {conta.saldo}")

