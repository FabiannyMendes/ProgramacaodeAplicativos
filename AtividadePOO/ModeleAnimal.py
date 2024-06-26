class Animal:
    def __init__(self, nome, dono, sexo, patas):
        self.nome = nome
        self.dono = dono
        self.sexo = sexo
        self.patas = patas

    def emitir_som(self):
        pass

    def mover(self):
        pass


class Dog(Animal):
    def __init__(self, nome, dono, sexo, patas, raca):
        super().__init__(nome, dono, sexo, patas)
        self.raca = raca

    def emitir_som(self):
        return "Woof!"

    def mover(self):
        return "Correndo como um cachorro"

# Test the Dog class
dog = Dog("Gustavo", "Fabi", "Macho", 4, "Vira lata")
print("Nome:", dog.nome)
print("Dono:", dog.dono)
print("Sexo:", dog.sexo)
print("Patas:", dog.patas)
print("Raça:", dog.raca)
print("Som emitido:", dog.emitir_som())
print("Movimento:", dog.mover())
