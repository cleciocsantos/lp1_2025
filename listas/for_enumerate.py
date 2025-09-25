L = [8, 9, 15]

print("Lendo valores em uma lista com FOR:")
for valor in L:
    print(valor)

print("\nLendo índices e valores em uma lista com FOR e ENUMERATE:")
for indice, valor in enumerate(L):
    print(f'O valor no índice {indice} é {valor}')

print("\nLendo valores em uma lista com WHILE:")
x = 0
while x < len(L):
    print(L[x])
    x += 1

print("\nUsando range com limite final:")
for x in range(3):
    print(x)

print("\nUsando range com indice inicial e limite final:")
for x in range(2,8):
    print(x)

print("\nUsando range com indice inicial, limite final e salto:")
for x in range(2,12,2):
    print(x)