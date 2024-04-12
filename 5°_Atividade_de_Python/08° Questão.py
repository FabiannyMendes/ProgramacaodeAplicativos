#8 - Escreva uma função chamada imprime_tabuada que aceita um número inteiro como parâmetro e imprime a tabuada desse número de 1 a 10.

def imprime_tabuada(numero):
    """
    Imprime a tabuada de um número de 1 a 10.

    Argumentos:
    numero: Um número inteiro.

    Retorna:
    Nada.
    """
    print("Tabuada de", numero, ":")
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)


numero = 7
imprime_tabuada(numero)
