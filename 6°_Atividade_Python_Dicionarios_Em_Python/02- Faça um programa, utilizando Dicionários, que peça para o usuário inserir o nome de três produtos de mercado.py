#2- Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

produtos = {}

for i in range(3):
  nome = input("Digite o nome do produto: ")
  preco = float(input("Digite o preço do produto: "))
  produtos[nome] = preco

print(produtos)
