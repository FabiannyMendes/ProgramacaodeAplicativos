#2. Crie uma classe que modele uma aluno (a) Atributos: nome, numero de matrıcula e curso (b) Metodos: mostrar curso e alterar curso

class Aluno:
  def _init_(self, nome, numero_matricula, curso):
    self.nome = nome
    self.numero_matricula = numero_matricula
    self.curso = curso

  def mostrar_curso(self):
    print(f"Curso: {self.curso}")

  def alterar_curso(self, novo_curso):
    self.curso = novo_curso

aluno = Aluno("Fabi", 6223, "Odontologia")

aluno.mostrar_curso()
aluno.alterar_curso("Biomedicina")
aluno.mostrar_curso()
