#8 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

def gerar_tabuada(numero):
    print(f'Tabuada de {numero}:')
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')

try:
    numero_input = int(input('Digite um número inteiro entre 1 e 10: '))

    if 1 <= numero_input <= 10:
        gerar_tabuada(numero_input)
    else:
        print('Por favor, digite um número entre 1 e 10.')
except ValueError:
    print('Por favor, digite um número inteiro válido.')
