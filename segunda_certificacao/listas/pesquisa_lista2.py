# Pesquisa utilizando while e sem a variável achou

lista = [8, 4, 7, 5, 2]
valor = int(input("Digite um valor: "))
x = 0
while x < len(lista):
    if lista[x] == valor:
        break
    x += 1
if x < len(lista):
    print(f'Achei o {valor} no índice {x}!')
else:
    print(f'Não achei o {valor}!')