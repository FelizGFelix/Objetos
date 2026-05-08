class Pet:
    def __init__(self, nome, especie, cuidador):
        self.nome = nome
        self.especie = especie
        self.cuidador = cuidador

    def animal(self):
        print(f"O {self.especie} se chama {self.nome} e seu cuidador é {self.cuidador}")


meupet1 = Pet("Rex", "cachorro", "Pedro")
meupet1.animal()

class Zoo(Pet):
    def __init__(self, nome, especie, cuidador, comer, area):
        super().__init__(nome, especie, cuidador)

        self.comer = comer
        self.area = area

    def zoologico(self):
        print(f"Ele fica na área {self.area} e se alimenta de {self.comer}")


animal1 = Zoo("Luiz", "macaco", "Lorenzo", "banana", 52)
animal1.animal()
animal1.zoologico()

    