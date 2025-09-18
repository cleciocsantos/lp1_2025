notas = [6.0,8.3,9.0,7.5,9.9,7.2,7.9]
soma = 0
x = 0
while x < len(notas):
    soma += notas[x]
    x += 1
media = soma/len(notas)
print(f'A média é {media:.1f}')

# Pergunta ao usuário uma nota para mostrar até que ele digite 0.
while True:
    posicao = int(input("Qual nota você deseja saber (de 1 a 7)? Digite 0 para sair. "))
    if posicao == 0:
        break
    if posicao >= 1 and posicao <= 7:
        print(f"A {posicao}º nota é {notas[posicao-1]}")
    else:
        print("Ei, se liga! Só pode de 1 a 7.")