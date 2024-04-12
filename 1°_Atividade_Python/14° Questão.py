#14 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que 
#custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

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
