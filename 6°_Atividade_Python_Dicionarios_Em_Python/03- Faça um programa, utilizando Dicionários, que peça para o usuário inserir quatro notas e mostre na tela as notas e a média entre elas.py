#3- Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.

notas = {}

for i in range(4):
  nota = float(input("Digite a nota: "))
  notas[f"nota{i+1}"] = nota

media = sum(notas.values()) / len(notas)

print(f"Notas: {notas}")
print(f"Média: {media}")
