# Crie uma função chamada dsa_calcula_imc que aceite dois argumentos: peso (em kg) e altura (em metros). A função deve calcular o Índice de Massa Corporal (IMC) usando a fórmula IMC=peso/altura^2 e retornar o valor do IMC

def calcula_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    if peso <= 0 or altura <= 0:
        print(f"Valor inválido")
    else:
        imc = peso / (altura * altura)
    print(f"Seu IMC é de: {imc:.2f}\n")

print(f"\n====== CALCULADORA DE IMC ======")
calcula_imc()