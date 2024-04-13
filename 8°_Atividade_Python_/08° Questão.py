#8. Crie uma classe que modele uma conta corrente (a) Atributos: numero da conta, nome do correntista e saldo (b) Metodos: alterar nome, deposito e saque; No construtor, saldo e opcional, com valor default zero e os demais atributos sao obrigatorios.

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
      print("Saldo insuficiente para saque.")

  def _str_(self):
    return f"Número da conta: {self.numero_conta}\nNome do correntista: {self.nome_correntista}\nSaldo: R${self.saldo:.2f}"
