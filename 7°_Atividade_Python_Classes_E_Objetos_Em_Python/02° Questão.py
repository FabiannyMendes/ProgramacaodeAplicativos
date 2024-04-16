#2- Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
  def _init_(self, lado_a, lado_b):
    self.lado_a = lado_a
    self.lado_b = lado_b

  def mudar_valor_lados(self, novo_lado_a, novo_lado_b):
    self.lado_a = novo_lado_a
    self.lado_b = novo_lado_b

  def retornar_valor_lados(self):
    return self.lado_a, self.lado_b

  def calcular_area(self):
    return self.lado_a * self.lado_b

  def calcular_perimetro(self):
    return 2 * (self.lado_a + self.lado_b)

lado_a = float(input("Informe a medida do lado A: "))
lado_b = float(input("Informe a medida do lado B: "))

retangulo = Retangulo(lado_a, lado_b)

area_local = retangulo.calcular_area()
area_piso = float(input("Informe a área de um piso: "))
quantidade_pisos = area_local / area_piso

print(f"Quantidade de pisos: {quantidade_pisos}")
