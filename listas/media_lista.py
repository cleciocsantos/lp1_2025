notas = [6.0,8.3,9.0,7.5,9.9,7.2,7.9]
soma = 0
x = 0
while x < len(notas):
    soma += notas[x]
    x += 1
media = soma/len(notas)
print(f'A média é {media}')