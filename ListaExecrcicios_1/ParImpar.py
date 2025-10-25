# Crie uma função que receba uma lista de números inteiros e retorne um dicionário contendo a contagem 
# de quantos números são pares e quantos são ímpares.

import random

def contar_pares_impares(numeros):
    pares = 0
    impares = 0

    for n in numeros:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

    return {"pares": pares, "impares": impares}

def gerar_lista_aleatoria(qtd, minimo=1, maximo=100):
    lista = [random.randint(minimo, maximo) for _ in range(qtd)]
    return lista

lista_numeros = gerar_lista_aleatoria(10, 1, 50)
print(f"\nLista gerada: {lista_numeros}")

resultado = contar_pares_impares(lista_numeros)
print(f"Resultado: {resultado}\n")