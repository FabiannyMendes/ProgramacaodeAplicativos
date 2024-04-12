#3 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


letra = input("Digite uma letra: ")

letra = letra.lower()

if letra.isalpha():
    if letra in 'aeiou':
        print(f'A letra {letra} é uma vogal.')
    else:
        print(f'A letra {letra} é uma consoante.')
else:
    print('Por favor, digite apenas uma letra do alfabeto.')
