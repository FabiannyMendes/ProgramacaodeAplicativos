#6. Implemente uma classe para representar em vetor (x,y,z) no R3 . Implemente os metodos para calcular a soma, subtracao, produto vetorial, produto escalar e modulo.

class Vetor3D:
  def _init_(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def _add_(self, other):
    return Vetor3D(self.x + other.x, self.y + other.y, self.z + other.z)

  def _sub_(self, other):
    return Vetor3D(self.x - other.x, self.y - other.y, self.z - other.z)

  def produto_vetorial(self, other):
    return Vetor3D(
      self.y * other.z - self.z * other.y,
      self.z * other.x - self.x * other.z,
      self.x * other.y - self.y * other.x
    )

  def produto_escalar(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z

  def modulo(self):
    return (self.x * 2 + self.y * 2 + self.z * 2) * 0.5

  def _str_(self):
    return f"({self.x}, {self.y}, {self.z})"

vetor1 = Vetor3D(1, 2, 3)
vetor2 = Vetor3D(4, 5, 6)

soma = vetor1 + vetor2
subtracao = vetor1 - vetor2
produto_vetorial = vetor1.produto_vetorial(vetor2)
produto_escalar = vetor1.produto_escalar(vetor2)
modulo_vetor1 = vetor1.modulo()

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Produto vetorial: {produto_vetorial}")
print(f"Produto escalar: {produto_escalar}")
print(f"Módulo do vetor 1: {modulo_vetor1}")
