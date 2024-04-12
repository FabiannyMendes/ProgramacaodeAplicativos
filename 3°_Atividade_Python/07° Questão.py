#7 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#Altere o programa anterior para mostrar no final a soma dos números.

def gerar_e_calcular_soma(num1, num2):
    inicio_intervalo = min(num1, num2)
    fim_intervalo = max(num1, num2)

    soma = 0

    for numero in range(inicio_intervalo, fim_intervalo + 1):
        print(numero, end=' ')
        soma += numero

    return soma

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

resultado_soma = gerar_e_calcular_soma(num1, num2)

print(f"\nA soma dos números no intervalo é: {resultado_soma}")
