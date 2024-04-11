#1 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Digite um valor: "))

if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")

#2 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


letra = input("Digite uma letra (F ou M): ")

letra = letra.upper()

if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")

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

#4 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#5 - Faça um Programa que leia três números e mostre o maior deles.


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3:
    maior_numero = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior_numero = numero2
else:
    maior_numero = numero3

print(f"O maior número é: {maior_numero}")

#6 - Faça um Programa que leia três números e mostre o maior e o menor deles.


def encontrar_maior_menor(num1, num2, num3):
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    return maior, menor

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    maior, menor = encontrar_maior_menor(num1, num2, num3)

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

main()

#7 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))

if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
    produto_mais_barato = "Produto 1"
    preco_mais_barato = preco_produto1
elif preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
    produto_mais_barato = "Produto 2"
    preco_mais_barato = preco_produto2
else:
    produto_mais_barato = "Produto 3"
    preco_mais_barato = preco_produto3

print(f"Você deve comprar o {produto_mais_barato}, pois é o mais barato, custando R${preco_mais_barato:.2f}.")

#8 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

def ordenar_decrescente(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    return numeros

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    numeros_ordenados = ordenar_decrescente(num1, num2, num3)

    print("Números em ordem decrescente:", numeros_ordenados)

if __name__ == "__main__":
    main()

#9 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

if salario_atual <= 280:
    percentual_aumento = 20
elif 280 < salario_atual <= 700:
    percentual_aumento = 15
elif 700 < salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = (percentual_aumento / 100) * salario_atual
novo_salario = salario_atual + aumento

print("\nResumo do reajuste salarial:")
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")

#10 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

def classificar_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return "Triângulo Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não é um triângulo"

lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

resultado = classificar_triangulo(lado1, lado2, lado3)
print("Resultado:", resultado)
