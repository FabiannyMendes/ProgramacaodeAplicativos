1) Questão. Uma classe é um tipo de estrutura de dados que define as características e
comportamentos de um objeto. Ela é uma espécie de molde a partir do qual os objetos
podem ser criados. Em linguagens de programação orientada a objetos, como Python ou
Java, as classes são fundamentais para organizar e estruturar o código.

2) Questão. Um método é uma função definida dentro de uma classe que descreve o
comportamento dos objetos dessa classe. Métodos podem acessar e modificar os atributos
da classe e podem interagir com outros objetos.

3) Questão. Uma função é um bloco de código que realiza uma tarefa específica e pode
retornar um valor. Em contraste com os métodos, as funções não estão associadas a uma
classe específica.

4) Questão
```python
def fibonacci_sequence(n):
sequence = [0, 1]
while len(sequence) < n:
next_term = sequence[-1] + sequence[-2]
sequence.append(next_term)
return sequence
```

5) Questão
Esta função recebe um número `n` como entrada e retorna uma lista com os primeiros `n`
termos da sequência de Fibonacci. Ela começa com os dois primeiros termos da sequência
(0 e 1) e, em seguida, calcula os próximos termos adicionando os dois últimos termos
calculados à lista até que a lista tenha `n` elementos.

6) Questão
```python
class Car:
def __init__(self, brand, model, year, color):
self.brand = brand
self.model = model
self.year = year
self.color = color
self.mileage = 0
self.engine_status = 'off'
def start_engine(self):
self.engine_status = 'on'
def stop_engine(self):
