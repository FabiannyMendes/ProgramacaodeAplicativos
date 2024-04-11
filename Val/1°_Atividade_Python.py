#1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print("Alo mundo")

#2 - Faça um Programa que peça um número e então mostre a mensagem

numero = input("Digite um número: ")
print("O número digitado foi:", numero)


#3 - Faça um Programa que peça dois números e imprima a soma.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma dos números é:", soma)


#4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média das notas é:", media)


#5 - Faça um Programa que converta metros para centímetros.

metros = float(input("Digite a medida em metros: "))
centimetros = metros * 100
print(f"{metros} metros é igual a {centimetros} centímetros")


#6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2)
print(f"A área do círculo é: {area}")


#7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o lado do quadrado: "))
area_quadrado = lado ** 2
dobro_area = 2 * area_quadrado
print(f"A área do quadrado é: {area_quadrado}")
print(f"O dobro da área do quadrado é: {dobro_area}")


#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_mensal = valor_por_hora * horas_trabalhadas
print(f"Seu salário no mês é: R${salario_mensal:.2f}")


#9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f"A temperatura em Celsius é: {celsius:.2f}°C")


#10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

#11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:


• o produto do dobro do primeiro com metade do segundo .
• a soma do triplo do primeiro com o terceiro.
• o terceiro elevado ao cubo.

num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

produto = (2 * num_int1) * (num_int2 / 2)
soma = (3 * num_int1) + num_real
cubo = num_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
print(f"O terceiro elevado ao cubo é: {cubo}")

#12 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável  (peso de peixes) e calcule o excesso. Gravar na variável  a quantidade de quilos além do limite e na variável  o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixes = float(input("Digite o peso dos peixes em quilos: "))
limite_peso = 50
excesso = max(0, peso_peixes - limite_peso)
multa = excesso * 4

print(f"Quantidade de quilos além do limite: {excesso:.2f} kg")
print(f"Valor da multa a ser pago: R${multa:.2f}")

#13 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:


• salário bruto.
• quanto pagou ao INSS.
• quanto pagou ao sindicato.
• o salário líquido.

calcule os descontos e o salário líquido, conforme a fórmula abaixo:
+ Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%) : R$  = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.


valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = valor_por_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Desconto do Imposto de Renda (11%): R${ir:.2f}")
print(f"Desconto do INSS (8%): R${inss:.2f}")
print(f"Desconto do Sindicato (5%): R${sindicato:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")

#15 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 6

litros_necessarios = tamanho_area / cobertura_por_litro

latas_necessarias = litros_necessarios / 18
preco_latas = latas_necessarias * 80

galoes_necessarios = litros_necessarios / 3.6
preco_galoes = galoes_necessarios * 25

mix_latas = int(latas_necessarias)
mix_galoes = round((litros_necessarios % 18) / 3.6)
preco_mix = (mix_latas * 80) + (mix_galoes * 25)

print(f"Comprar apenas latas de 18 litros: {latas_necessarias:.2f} latas, Preço: R${preco_latas:.2f}")
print(f"Comprar apenas galões de 3,6 litros: {galoes_necessarios:.2f} galões, Preço: R${preco_galoes:.2f}")
print(f"Misturar latas e galões: {mix_latas} latas e {mix_galoes} galões, Preço: R${preco_mix:.2f}")


#16 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

• comprar apenas latas de 18 litros;
• comprar apenas galões de 3,6 litros;
• misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


#17 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Digite o tamanho do arquivo para download em MB: "))
velocidade_internet = float(input("Digite a velocidade do link de Internet em Mbps: "))

tempo_aproximado = (tamanho_arquivo / (velocidade_internet / 8)) / 60

print(f"Tempo aproximado de download: {tempo_aproximado:.2f} minutos")
