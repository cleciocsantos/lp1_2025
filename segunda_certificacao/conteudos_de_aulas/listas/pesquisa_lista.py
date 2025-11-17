# Pesquisa utilizando while e uma variável achou

lista = [8, 4, 7, 5, 2]
valor = int(input("Digite um valor: "))
achei = False
x = 0
while x < len(lista):
    if lista[x] == valor:
        achei = True
        break
    x += 1
if achei:
    print(f'Achei o {valor} no índice {x}!')
else:
    print(f'Não achei o {valor}!')