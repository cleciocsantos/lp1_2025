import random
def gerar_notas():
    notas = []
    for aluno in range(10):
        nota = random.randint(0,10)
        notas.append(nota)
    return notas

def calcular_estatisticas(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma/len(notas)
    maiorNota = max(notas)
    menorNota = min(notas)
    qtdAcimaDaMedia = 0
    for nota in notas:
        if nota >= media:
            qtdAcimaDaMedia += 1
    qtdDeAprovados = 0
    for nota in notas:
        if nota >= 6:
            qtdDeAprovados += 1
    qtDeReprovados = len(notas) - qtdDeAprovados
    return media, maiorNota, menorNota, qtdAcimaDaMedia, qtdDeAprovados, qtDeReprovados


notas = gerar_notas()
media, maiorNota, menorNota, qtdAcimaDaMedia, qtdDeAprovados, qtDeReprovados = calcular_estatisticas(notas)

print(notas)
print(media, maiorNota, menorNota, qtdAcimaDaMedia, qtdDeAprovados, qtDeReprovados)
