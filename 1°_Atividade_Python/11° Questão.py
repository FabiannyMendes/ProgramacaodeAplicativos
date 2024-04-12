#11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#* o produto do dobro do primeiro com metade do segundo .
#* a soma do triplo do primeiro com o terceiro.
#* o terceiro elevado ao cubo.

num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

produto = (2 * num_int1) * (num_int2 / 2)
soma = (3 * num_int1) + num_real
cubo = num_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
print(f"O terceiro elevado ao cubo é: {cubo}")
