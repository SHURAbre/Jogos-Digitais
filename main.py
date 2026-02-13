import random

class Tank:

    def __init__(self, nome):
        self.nome = nome
        self.vida = 60
        self.municao = 5
        self.vivo = True

    def mostrar(self):
        if self.vivo:
            print(self.nome, "- Vida:", self.vida, "| Munição:", self.municao)
        else:
            print(self.nome, "- DESTRUIDO")

    def levar_tiro(self):
        self.vida -= 20
        print(self.nome, "levou um tiro!")

        if self.vida <= 0:
            self.vivo = False
            print(self.nome, "EXPLODIU!")

    def atirar(self, inimigo):
        if self.municao > 0:
            self.municao -= 1
            print(self.nome, "atirou em", inimigo.nome)
            inimigo.levar_tiro()
        else:
            print(self.nome, "sem munição!")


tanques = []

while True:
    try:
        qtd = int(input("Quantos tanques (2 a 10)? "))
        if 2 <= qtd <= 10:
            break
        else:
            print("Digite um número entre 2 e 10.")
    except:
        print("Digite apenas números inteiros.")

for i in range(qtd):
    nome = input("Nome do tanque: ")
    t = Tank(nome)
    tanques.append(t)

print("\nBATALHA INICIADA")

while len(tanques) > 1:

    print("\n--- NOVA RODADA ---")

    ordem = tanques.copy()
    random.shuffle(ordem)

    for jogador in ordem:

        if jogador.vivo == False:
            continue

        if len(tanques) == 1:
            break

        print("\nVez de:", jogador.nome)

        for i in range(len(tanques)):
            if tanques[i] != jogador:
                print(i, "-", tanques[i].nome)

        while True:
            try:
                alvo_i = int(input("Escolha o alvo: "))
                if (
                    0 <= alvo_i < len(tanques)
                    and tanques[alvo_i] != jogador
                ):
                    break
                else:
                    print("Alvo inválido.")
            except:
                print("Digite apenas números.")

        alvo = tanques[alvo_i]

        jogador.atirar(alvo)

        if alvo.vivo == False:
            print(alvo.nome, "foi destruído!")
            tanques.remove(alvo)

    print("\nSTATUS:")
    for t in tanques:
        t.mostrar()

print("\nVENCEDOR:", tanques[0].nome)