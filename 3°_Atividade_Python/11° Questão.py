#11 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

def fibonacci(n):
    fib_series = [1, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series[:n]

n = 10
resultado = fibonacci(n)
print(f"A série de Fibonacci até o {n}-ésimo termo é: {resultado}")
