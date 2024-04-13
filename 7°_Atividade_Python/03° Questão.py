#3- Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
  def _init_(self, nome, idade, peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura

  def envelhecer(self):
    self.idade += 1
    if self.idade < 21:
      self.crescer(0.5)

  def engordar(self, peso):
    self.peso += peso

  def emagrecer(self, peso):
    self.peso -= peso

  def crescer(self, altura):
    self.altura += altura

pessoa = Pessoa("Camila", 17, 76, 1.60)
pessoa.envelhecer()
pessoa.engordar(5)
pessoa.emagrecer(2)
pessoa.crescer(0.3)

print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")
print(f"Peso: {pessoa.peso}")
print(f"Altura: {pessoa.altura}")
