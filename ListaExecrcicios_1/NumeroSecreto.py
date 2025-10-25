# Crie um jogo onde o computador escolhe um número secreto entre 1 e 20. O jogador tem 5 tentativas 
# para adivinhar. A cada tentativa, o programa informa se o palpite foi muito alto ou muito baixo. 
# Se o jogador acertar, o loop deve ser interrompido com uma mensagem de vitória.

import random                                        # módulo para gerar números aleatórios
numero_secreto = random.randint(1, 20)               # o computador escolhe um número secreto entre 1 e 20
tentativas = 5                                       # número máximo de chances

print("\n🎮 Bem-vindo ao jogo da adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 20.")
print(f"Você tem {tentativas} tentativas.\n")

# loop para as tentativas
for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite → "))

    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto}\n")
        break  # encerra o loop se acertar
    elif palpite < numero_secreto:
        print("📉 Muito baixo! Tente um número maior.\n")
    else:
        print("📈 Muito alto! Tente um número menor.\n")

# se o jogador não acertar em 5 tentativas
else:
    print(f"😢 Suas tentativas acabaram! O número secreto era {numero_secreto}.\n")

print(f"-" *50)