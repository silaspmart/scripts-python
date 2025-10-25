# Dada uma lista de números, crie uma nova lista usando list comprehension que contenha o quadrado 
# de cada número par da lista original

def quadrados_pares(lista):
    return [x ** 2 for x in lista if x % 2 == 0]

numeros = list(range(1, 16))
resultado = quadrados_pares(numeros)

print(f"*" * 100)
print(f"A lista de números é: {numeros}")
print(f"O quadrado dos números pares é: {resultado}")
print(f"*" * 100)