#3 - Escreva uma função chamada verifica_primo que verifica se um número é primo ou não e retorna True ou False.

def verifica_primo(num):
    """
    Verifica se um número é primo ou não.

    Argumentos:
    num: Um número inteiro.

    Retorna:
    True se o número for primo, False caso contrário.
    """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

numero = 17
if verifica_primo(numero):
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")
