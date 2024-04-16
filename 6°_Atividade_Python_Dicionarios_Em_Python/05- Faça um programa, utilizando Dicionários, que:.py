#5- Faça um programa, utilizando Dicionários, que:

#1° Passo: Peça para o usuário inserir o nome de três funcionários e os mostre na tela.
#2° Passo: Peça para o usuário demitir um funcionário e mostre na tela os funcionários restantes.

funcionarios = {}

for i in range(3):
  nome = input(f"Digite o nome do {i+1}º funcionário: ")
  funcionarios[f"funcionario{i+1}"] = nome

print(f"Funcionários: {funcionarios}")

nome_demitido = input("Digite o nome do funcionário que deseja demitir: ")

if nome_demitido not in funcionarios.values():
  print(f"Funcionário {nome_demitido} não encontrado.")
else:
  for key, value in funcionarios.items():
    if value == nome_demitido:
      del funcionarios[key]
      break

  print(f"Funcionários restantes: {funcionarios}")
