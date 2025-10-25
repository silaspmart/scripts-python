# Você tem uma lista de dicionários, onde cada dicionário representa uma pessoa com nome e idade. 
# Use a função sorted() com uma expressão lambda como chave (key) para ordenar a lista de pessoas 
# da mais nova para a mais velha.

def ordenar_pessoas_por_idade(pessoas):
    print("📋 Lista original:")
    for nome, idade in pessoas.items():
        print(f"{nome} - {idade} anos")

    print("\n📊 Lista ordenada por idade (crescente):")
    pessoas_ordenadas = sorted(pessoas.items(), key=lambda item: item[1])
    for nome, idade in pessoas_ordenadas:
        print(f"{nome} - {idade} anos")

pessoas = {"João": 31,"Wilson": 28,"Analine": 26,
           "Carla": 35,"Joana": 42,"Roberval": 29,
           "Maria": 62,"Daiana": 52,"Bianca": 21
          }

ordenar_pessoas_por_idade(pessoas)