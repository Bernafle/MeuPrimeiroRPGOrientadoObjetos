import random 

#classe ou super classe pai
class Personagem():

  #construtor
  def __init__(self,nome: str, classe: str, vida: int, ataque: int):
    self.nome:  str = nome 
    self.classe:  str = classe
    self.vida:  int = vida
    self.ataque:  int = ataque

    def ataque(self, alvo):
      dano = random.randint(1, self.ataque)
      alvo.receber_danp(dano)
      print(f"{self.nome} atacou { alvo.nome} e causou {dano} de dano!")

    def receber_dano(self, dano: int):
      self.vida -= dano

    def esta_vivo(self):
      return self.vida > 0


class paladino(personagem):

  def __int__(self, nome):
    super().__init__(nome, "paladino", 100,20)

class mago(personagem):

  def __int__(self, nome):
    super().__init__(nome, "mago", 80,30)

class Elfo(personagem):

  def __int__(self, nome):
    super().__init__(nome, "Elfo", 100,20)

class Humano(personagem):

  def __int__(self, nome):
    super().__init__(nome, "Humano", 110, 18)

class Orc(personagem):

  def __int__(self, nome):
    super().__init__(nome, "Orc", 150,15)