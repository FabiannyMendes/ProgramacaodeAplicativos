#4- Faça um programa, utilizando Dicionários, que:

#1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
#2° Passo: Peça para o usuário inserir um número.
#3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário..

caixa_misteriosa = {}

for i in range(4):
  item = input(f"Digite o {i+1}º item para colocar na caixa misteriosa: ")
  caixa_misteriosa[f"item{i+1}"] = item

numero = int(input("Digite um número entre 1 e 4: "))

if not 1 <= numero <= 4:
  print("Número inválido. Digite um número entre 1 e 4.")
else:
  item = caixa_misteriosa[f"item{numero}"]
  print(f"O item na posição {numero} é: {item}")
