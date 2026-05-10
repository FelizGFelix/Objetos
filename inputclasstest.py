import os
def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)


class Usuario:
    def __init__(self):
        self.nome = ""
        self.email = ""
        self.senha = ""

    def criar_conta(self):
        self.nome = input("Digite o seu nome de usuario: ")
        self.email = input("Digite o seu email: ")
        self.senha = input("Digite a sua senha: ")

        limpar()

        print(f"Informações da conta:\nNome:{self.nome}\nEmail:{self.email}\nSenha:{self.senha}")

usuario1 = Usuario()
usuario1.criar_conta()
