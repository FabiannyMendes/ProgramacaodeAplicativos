#13 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return f'O fatorial de {numero} é {fatorial}.'

try:
    numero_usuario = int(input("Digite um número inteiro para calcular o fatorial: "))
    resultado = calcular_fatorial(numero_usuario)
    print(resultado)
except ValueError:
    print("Por favor, insira um número inteiro válido.")
