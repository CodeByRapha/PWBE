class Personagem:
    def __init__(self, nome, saude, forca, defesa):
        self.nome = nome
        self.saude = saude
        self.forca = forca
        self.defesa = defesa
        self.xp = 0  # experiência do personagem

    def atacar(self, inimigo):
        dano = max(self.forca - inimigo.defesa, 0)  # calcula o dano causado
        inimigo.saude -= dano  # reduz a saúde do inimigo
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")

    def usar_pocao(self):
        self.saude += 20  # recupera 20 de vida
        print(f"{self.nome} usou poção e recuperou 20 de saúde.")

    def esta_vivo(self):
        return self.saude > 0  # retorna se ainda está vivo

    def ganhar_xp(self, pontos):
        self.xp += pontos  # soma pontos de experiência
        print(f"{self.nome} ganhou {pontos} XP!")

# Combate exemplo
p1 = Personagem("Herói", 100, 30, 10)
p2 = Personagem("Vilão", 80, 25, 8)

p1.atacar(p2)
p2.usar_pocao()
p2.atacar(p1)

if not p2.esta_vivo():
    p1.ganhar_xp(50)
