class Restaunte():
    def __init__(self, nome, tipo, especialidade, local, nota):
        self.nome = nome
        self.tipo = tipo
        self.especialidade = especialidade
        self.local = local
        self.nota = nota

    def apresentação(self):
        print(f"Olá, somos o restaurente {self.nome} e nossa especialidade é {self.especialidade}")

    def descricao(self):
        print(f"Somos um restaurante nota {self.nota} de tipo {self.tipo} e estamos situados em {self.local}")


meu_restaurente = Restaunte("Master Chef Pizza", "Rodizio", "Pizzas variadas", "Rua João Florindo Zanetti", 4.5)

meu_restaurente.apresentação()
meu_restaurente.descricao()