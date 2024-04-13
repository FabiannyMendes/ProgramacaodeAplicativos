#1- Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
  def _init_(self, lado):
    self.lado = lado

  def mudar_valor_lado(self, novo_lado):
    self.lado = novo_lado

  def retornar_valor_lado(self):
    return self.lado

  def calcular_area(self):
    return self.lado ** 2

quadrado = Quadrado(5)

quadrado.mudar_valor_lado(30)

print(quadrado.retornar_valor_lado())

print(quadrado.calcular_area())

