#6 - Faça um Programa que leia três números e mostre o maior e o menor deles.


def encontrar_maior_menor(num1, num2, num3):
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    return maior, menor

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    maior, menor = encontrar_maior_menor(num1, num2, num3)

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

main()
