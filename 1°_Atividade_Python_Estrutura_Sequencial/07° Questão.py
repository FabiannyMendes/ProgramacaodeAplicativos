#7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o lado do quadrado: "))
area_quadrado = lado ** 2
dobro_area = 2 * area_quadrado
print(f"A área do quadrado é: {area_quadrado}")
print(f"O dobro da área do quadrado é: {dobro_area}")
