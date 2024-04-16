#4. Crie uma classe para representar um numero complexo. Implemente, usando sobrecarga de operador, os metodos para fazer as operacoes de soma, subtracao e produto entre dois numeros

class NumeroComplexo:
  def _init_(self, real, imag):
    self.real = real
    self.imag = imag

  def _add_(self, other):
    return NumeroComplexo(self.real + other.real, self.imag + other.imag)

  def _sub_(self, other):
    return NumeroComplexo(self.real - other.real, self.imag - other.imag)

  def _mul_(self, other):
    return NumeroComplexo(
      self.real * other.real - self.imag * other.imag,
      self.real * other.imag + self.imag * other.real
    )

  def _str_(self):
    return f"{self.real} + {self.imag}i"

numero1 = NumeroComplexo(2, 3)
numero2 = NumeroComplexo(4, 5)

soma = numero1 + numero2
diferenca = numero1 - numero2
produto = numero1 * numero2

print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Produto: {produto}")
