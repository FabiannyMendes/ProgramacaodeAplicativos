#3 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
#vetor_1 = []
#vetor_2 = []

for i in range(10):
  valor = int(input(f"Digite o {i+1}º elemento do primeiro vetor: "))
  vetor_1.append(valor)

for i in range(10):
  valor = int(input(f"Digite o {i+1}º elemento do segundo vetor: "))
  vetor_2.append(valor)

vetor_3 = []

for i in range(10):
  vetor_3.append(vetor_1[i])
  vetor_3.append(vetor_2[i])

print(f"Terceiro vetor: {vetor_3}")
