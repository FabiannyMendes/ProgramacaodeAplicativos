#4 - Faça um programa que leia 5 números e informe o maior número.

maior_numero = None

for i in range(5):
    numero = float(input(f'Digite o {i+1}º número: '))

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

print(f'O maior número é: {maior_numero}')
