#5 - Foram anotadas as idades e alturas de 10 alunos. 
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
#idades = []
#alturas = []

for i in range(10):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    altura = float(input(f"Digite a altura do aluno {i + 1} (em metros): "))
    idades.append(idade)
    alturas.append(altura)

media_alturas = sum(alturas) / 10
alunos_acima_13_com_altura_abaixo_media = sum(1 for i in range(10) if idades[i] > 13 and alturas[i] < media_alturas)

print(f"\n{alunos_acima_13_com_altura_abaixo_media} alunos com mais de 13 anos possuem altura inferior à média.")
