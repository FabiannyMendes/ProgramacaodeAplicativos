#5. Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os metodos para fazer as operacoes de incremento (de segundos) no horario e diferenca entre dois horarios.

class Horario:
  def _init_(self, hora, minuto, segundo):
    self.hora = hora
    self.minuto = minuto
    self.segundo = segundo

  def incrementar(self, segundos):
    self.segundo += segundos
    self.__ajustar_tempo()

  def diferenca(self, outro_horario):
    segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo
    segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
    return segundos_self - segundos_outro

  def __ajustar_tempo(self):
    if self.segundo >= 60:
      self.minuto += self.segundo // 60
      self.segundo %= 60
    if self.minuto >= 60:
      self.hora += self.minuto // 60
      self.minuto %= 60

  def _str_(self):
    return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

horario1 = Horario(10, 30, 0)
horario2 = Horario(11, 45, 0)

horario1.incrementar(3600)

diferenca = horario2.diferenca(horario1)

print(f"Horário 1 após incremento: {horario1}")
print(f"Diferença entre horários: {diferenca} segundos")
