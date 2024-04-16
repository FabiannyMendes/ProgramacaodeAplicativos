#15 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#* comprar apenas latas de 18 litros;
#* comprar apenas galões de 3,6 litros;
#* misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input("Enter the area to be painted in square meters: "))
liters_needed = area / 6

num_cans = math.ceil(liters_needed / 18)
num_gallons = math.ceil((liters_needed % 18) / 3.6)

cost_cans = num_cans * 80
cost_gallons = num_gallons * 25
total_cost = cost_cans + cost_gallons

print(f"Number of cans: {num_cans}")
print(f"Number of gallons: {num_gallons}")
print(f"Total cost: R${total_cost:.2f}")
