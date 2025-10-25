# Dada uma lista de frases, use a função map() em conjunto com uma expressão lambda para criar uma 
# nova lista onde cada frase é convertida para letras maiúsculas e tem a palavra "PYTHON" anexada ao final.

frases = [
    "programar é divertido",
    "estou aprendendo lambda",
    "adoro desafios de lógica"
]

novas_frases = list(map(lambda f: f.upper() + " PYTHON", frases))

for frase in novas_frases:
    print(frase)