#1. Crie uma classe que modele uma pessoa
#(a) Atributos: nome, idade e endereco
#(b) Metodos: mostrar endereco e alterar endereco

class Pessoa:
  def _init_(self, nome, idade, endereco):
    self.nome = nome
    self.idade = idade
    self.endereco = endereco

  def mostrar_endereco(self):
    print(f"Endereço: {self.endereco}")

  def alterar_endereco(self, novo_endereco):
    self.endereco = novo_endereco

pessoa = Pessoa("Fabianny", 17, "73 Recife")

pessoa.mostrar_endereco()
pessoa.alterar_endereco("825 Janga")
pessoa.mostrar_endereco()
