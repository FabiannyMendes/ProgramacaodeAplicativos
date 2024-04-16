#3. Crie uma classe representando os alunos de um determinado curso. A classe deve conter os atributos matrıcula do aluno, nome, nota da primeira prova, nota da segunda prova e nota da terceira prova. Crie metodos para acessar o nome e a media do aluno.  (a) Permita ao usuario entrar com os dados de 5 alunos.  (b) Encontre o aluno com maior media geral.  (c) Encontre o aluno com menor media geral  (d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para aprovacao.

class Aluno:
  def _init_(self, matricula, nome, nota1, nota2, nota3):
    self.matricula = matricula
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.nota3 = nota3

  def get_nome(self):
    return self.nome

  def get_media(self):
    return (self.nota1 + self.nota2 + self.nota3) / 3

alunos = []

for i in range(5):
  matricula = int(input("Digite a matrícula do aluno: "))
  nome = input("Digite o nome do aluno: ")
  nota1 = float(input("Digite a nota da primeira prova: "))
  nota2 = float(input("Digite a nota da segunda prova: "))
  nota3 = float(input("Digite a nota da terceira prova: "))
  alunos.append(Aluno(matricula, nome, nota1, nota2, nota3))

maior_media = 0
aluno_maior_media = None
for aluno in alunos:
  media = aluno.get_media()
  if media > maior_media:
    maior_media = media
    aluno_maior_media = aluno

menor_media = 10
aluno_menor_media = None
for aluno in alunos:
  media = aluno.get_media()
  if media < menor_media:
    menor_media = media
    aluno_menor_media = aluno

print(f"Aluno com maior média: {aluno_maior_media.nome} - Média: {maior_media}")
print(f"Aluno com menor média: {aluno_menor_media.nome} - Média: {menor_media}")
