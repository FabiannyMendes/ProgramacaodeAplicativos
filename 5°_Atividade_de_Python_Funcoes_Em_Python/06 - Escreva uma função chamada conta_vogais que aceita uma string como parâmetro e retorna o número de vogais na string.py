#6 - Escreva uma função chamada conta_vogais que aceita uma string como parâmetro e retorna o número de vogais na string.

def conta_vogais(string):
    """
    Conta o número de vogais em uma string.

    Argumentos:
    string: Uma string.

    Retorna:
    O número de vogais na string.
    """
    vogais = "aeiouAEIOU"
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador

texto = "Python é uma linguagem de programação"
print("O número de vogais no texto é:", conta_vogais(texto))
