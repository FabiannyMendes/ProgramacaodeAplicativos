#5 - Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3:
    maior_numero = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior_numero = numero2
else:
    maior_numero = numero3

print(f"O maior número é: {maior_numero}")
