#9. Um racional e qualquer numero da forma p/q, sendo p inteiro e q inteiro nao nulo. Crie uma classe para representar um racional e os seguinte metodos: 1 (a) inverter sinal; (b) somar dois racionais; (c) subtrair dois racionais; (d) produto de dois racionais; (e) quociente de dois racionais;

class Racional:
  def _init_(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador

  def _str_(self):
    return f"{self.numerador}/{self.denominador}"

  def sinal_contrario(self):
    return Racional(-self.numerador, self.denominador)

  def somar(self, outro_racional):
    numerador = self.numerador * outro_racional.denominador + outro_racional.numerador * self.denominador
    denominador = self.denominador * outro_racional.denominador
    return Racional(numerador, denominador).simplificar()

  def subtrair(self, outro_racional):
    numerador = self.numerador * outro_racional.denominador - outro_racional.numerador * self.denominador
    denominador = self.denominador * outro_racional.denominador
    return Racional(numerador, denominador).simplificar()

  def multiplicar(self, outro_racional):
    numerador = self.numerador * outro_racional.numerador
    denominador = self.denominador * outro_racional.denominador
    return Racional(numerador, denominador).simplificar()

  def dividir(self, outro_racional):
    numerador = self.numerador * outro_racional.denominador
    denominador = self.denominador * outro_racional.numerador
    return Racional(numerador, denominador).simplificar()

  def simplificar(self):
    divisor = self.mdc(self.numerador, self.denominador)
    self.numerador //= divisor
    self.denominador //= divisor
    return self

  def mdc(self, a, b):
    while b != 0:
      a, b = b, a % b
    return a
