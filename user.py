class User():
    def __init__(self, nome, bio, online):
        self.nome = nome
        self.bio = bio
        self.online = online

    def perfil(self):
        print(f"{self.nome}\n{self.bio}\nPerfil aberto:{self.online}")
        
my_profile = User ("Felix Lain", "um cara legal", True)
my_profile.perfil()