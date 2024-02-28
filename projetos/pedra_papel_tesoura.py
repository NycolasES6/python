from random import choice

def escolha_maquina() :
    return choice(["pedra", "papel", "tesoura"])

print(escolha_maquina())