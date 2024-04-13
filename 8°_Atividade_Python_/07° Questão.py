#7. Crie uma classe que modele um carro (a) Atributos: marca, ano e preco (b) Metodos: mostrar preco e de exibicao dos dados Leia os dados de 5 carros e um valor p, Mostre as informacoes de todos os carros com preco menor que p.

class Carro:
  def _init_(self, marca, ano, preco):
    self.marca = marca
    self.ano = ano
    self.preco = preco

  def mostrar_preco(self):
    print(f"Preço: R${self.preco:.2f}")

  def _str_(self):
    return f"Marca: {self.marca}\nAno: {self.ano}\nPreço: R${self.preco:.2f}"

carros = []

for i in range(5):
  marca = input("Digite a marca do carro: ")
  ano = int(input("Digite o ano do carro: "))
  preco = float(input("Digite o preço do carro: "))
  carros.append(Carro(marca, ano, preco))

p = float(input("Digite o valor p: "))

print(f"\nCarros com preço menor que R${p:.2f}:")
for carro in carros:
  if carro.preco < p:
    print(carro)
