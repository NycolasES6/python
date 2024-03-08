from random import choice

def escolha_maquina() :
    return choice(["PEDRA", "PAPEL", "TESOURA", "PAPEL", "PEDRA", "TESOURA"])

def escolha_jogador() :
    escolha = input("Qual a sua escolha ? \n PEDRA \n PAPEL \n TESOURA \n ? ")
    escolha = escolha.upper()

    while escolha not in ["PEDRA", "PAPEL", "TESOURA"]:
        print("Escolha inválida !! \n")
        escolha = input("Qual a sua escolha ? \n PEDRA \n PAPEL \n TESOURA \n ? ")
        escolha = escolha.upper()

    return escolha

quer_jogar = input("Quer jogar comigo ? \n [ s ] - SIM \n [ n ] NAO \n ? ").upper()

if quer_jogar in ["S", "SIM"] :
    quer_jogar = True
else:
    quer_jogar = False
    print("Ficou com medo ?")

while quer_jogar :
    print("A partida começou -----------------")
    escolha_do_jogador = escolha_jogador()
    escolha_da_maquina = escolha_maquina()

    print(f,"Escolha do jogador foi {escolha_do_jogador}")
    print(escolha_da_maquina)
