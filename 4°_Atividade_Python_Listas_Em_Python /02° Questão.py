#2 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor_a = [int(input(f"Digite o número {i + 1}: ")) for i in range(10)]

soma_quadrados = sum(x**2 for x in vetor_a)
print(f"\nA soma dos quadrados dos elementos do vetor é: {soma_quadrados}")
