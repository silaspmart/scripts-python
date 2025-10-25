# Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas. 
# Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos
#  que tiveram nota acima da média.

def alunosAcimaDaMedia (alunos):
    media = sum(alunos.values()) / len(alunos)
    acimaMedia = []

    for aluno, nota in alunos.items():
        if nota > media:
            acimaMedia.append(aluno)

    print(f"\nMédia da turma: {media:.2f}")
    print(f"Alunos acima da média: ")

    for aluno in acimaMedia:
        print(f"- {aluno}")

alunos = {"João": 6, "José": 8, "Maria": 7, "Alice": 5}
alunosAcimaDaMedia (alunos) 
print(f"-" * 50)