#7 - Escreva uma função chamada soma_quadrados que aceita uma lista de números como parâmetro e retorna a soma dos quadrados desses números.

def soma_quadrados(lista):
    """
    Calcula a soma dos quadrados dos números em uma lista.

    Argumentos:
    lista: Uma lista de números.

    Retorna:
    A soma dos quadrados dos números na lista.
    """
    soma = 0
    for num in lista:
        soma += num ** 2
    return soma

numeros = [1, 2, 3, 4, 5]
print("A soma dos quadrados dos números na lista é:", soma_quadrados(numeros))
