# Escreva uma função que receba os valores de três lados de um triângulo e o classifique como:
#  "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

def classificar_triangulo(lado1, lado2, lado3):
    
    if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado2 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Inválido (os lados não formam um triângulo)"

print("=== CLASSIFICADOR DE TRIÂNGULOS ===\n")

lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))

resultado = classificar_triangulo(lado1, lado2, lado3)
print(f"\nO triângulo é: {resultado}")