#10 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros_pares = 0
numeros_impares = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))

    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print(f"\nQuantidade de números pares: {numeros_pares}")
print(f"Quantidade de números ímpares: {numeros_impares}")
