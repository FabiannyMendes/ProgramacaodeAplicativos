#5- Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Televisor:
  def _init_(self):
    self.canal = 1
    self.volume = 12

  def aumentar_volume(self):
    if self.volume < 100:
      self.volume += 1

  def diminuir_volume(self):
    if self.volume > 0:
      self.volume -= 1

  def mudar_canal(self, novo_canal):
    if 1 <= novo_canal <= 99:
      self.canal = novo_canal

televisor = Televisor()
televisor.aumentar_volume()
televisor.diminuir_volume()
televisor.mudar_canal(52)

print(f"Canal: {televisor.canal}")
print(f"Volume: {televisor.volume}")
