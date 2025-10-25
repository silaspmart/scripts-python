print("*" * 50)
print("--- Jogo Pedra, Papel e Tesoura (2 Jogadores) ---\n================| REGRAS |================")
print("Escolham entre: \n1) PEDRA\n2) PAPEL\n3) TESOURA")
print("*" * 50)
opcoesValidas = ("pedra", "papel", "tesoura")

jogador1 = input("JOGADOR 1! \nDigite a sua escolha: ")
jogador2 = input("JOGADOR 2! \nDigite a sua escolha: ")

jogada1 = jogador1.lower().strip()
jogada2 = jogador2.lower().strip()

print("*" * 50)
print(f"O jogador 1 escolheu: {jogada1}")  
print(f"O jogador 2 escolheu: {jogada2}")  
print("*" * 50)

if jogada1 not in opcoesValidas or jogada2 not in opcoesValidas:
    print("Uma ou ambas jogadas são inválidas!")
elif jogada1 == jogada2:
    print("Houve um empate!")
elif jogada1 == "pedra" and jogada2 == "tesoura":
    print("O jogador 1 venceu!")
elif jogada1 == "tesoura" and jogada2 == "papel":
    print("O jogador 1 venceu!")
elif jogada1 == "papel" and jogada2 == "pedra":
    print("O jogador 1 venceu!")
else:
    print("O jogador 2 venceu!")

print("*" * 50)
print("================| FIM DE JOGO!!! |================")