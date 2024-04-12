#4 - Escreva uma função chamada inverte_string que aceita uma string como parâmetro e retorna a string invertida.

def inverte_string(string):
    """
    Inverte uma string.

    Argumentos:
    string: Uma string.

    Retorna:
    A string invertida.
    """
    return string[::-1]


texto = "Olá, mundo!"
texto_invertido = inverte_string(texto)
print("String original:", texto)
print("String invertida:", texto_invertido)
