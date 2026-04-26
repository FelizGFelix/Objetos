class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Name(self):
        print(f"O nome do meu cachorro é {self.name} e tem {self.age} anos")

    def Sit(self):
        print(f"{self.name} está sentado")

    def Roll(self):
        print(f"{self.name} está rolando")

mydog = Dog("Willie", 6)
mydog.Name()
mydog.Sit()
mydog.Roll()

yourdog = Dog("Lucy", 3)
yourdog.Sit()
yourdog.Roll()