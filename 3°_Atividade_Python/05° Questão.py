#5 - Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
media = 0

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero

media = soma / 5

print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")
