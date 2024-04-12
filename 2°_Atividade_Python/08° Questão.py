#8 - Faça um Programa que leia três números e mostre-os em ordem decrescente.


def ordenar_decrescente(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    return numeros

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    numeros_ordenados = ordenar_decrescente(num1, num2, num3)

    print("Números em ordem decrescente:", numeros_ordenados)

if __name__ == "__main__":
    main()
