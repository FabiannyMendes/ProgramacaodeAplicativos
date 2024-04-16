#2 - Escreva uma função chamada fatorial que calcula o fatorial de um número inteiro fornecido como argumento

def fatorial(n):
    """
    Calcula o fatorial de um número inteiro n.

    Argumentos:
    n: Um número inteiro.

    Retorna:
    O fatorial de n.
    """
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


numero = 5
print("O fatorial de", numero, "é:", fatorial(numero))

