#5 - Escreva uma função chamada maior_valor que aceita uma lista de números como parâmetro e retorna o maior valor na lista.

def maior_valor(lista):
    """
    Retorna o maior valor em uma lista de números.

    Argumentos:
    lista: Uma lista de números.

    Retorna:
    O maior valor na lista.
    """
    if not lista:
        return None

    max_valor = lista[0]
    for num in lista:
        if num > max_valor:
            max_valor = num
    return max_valor


numeros = [10, 5, 20, 15, 30]
print("O maior valor na lista é:", maior_valor(numeros))
