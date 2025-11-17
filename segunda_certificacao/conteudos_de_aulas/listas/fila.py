fila = []
#inserindo elementos na fila
fila.append("Renan")
fila.append("Igor")
fila.append("Alicia")

#removendo elementos da fila
while len(fila) != 0:
    aluno = fila.pop(0)
    print(f'Removi {aluno} da fila.')
