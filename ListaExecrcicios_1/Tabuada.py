# Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.

def tabuada (numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

print(f"=== TABUADA INTERATIVA ===\n")
numero = int(input(f"Digite um numero para saber a sua tabuada: "))

tabuada(numero)
print(f"-" *50)