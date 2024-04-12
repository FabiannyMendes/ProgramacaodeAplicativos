#9 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.


def calcular_potencia(base, expoente):
    resultado = 1

    for _ in range(expoente):
        resultado *= base

    return resultado

base = float(input("Digite o número base: "))
expoente = int(input("Digite o número do expoente: "))

resultado = calcular_potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a {resultado}")
