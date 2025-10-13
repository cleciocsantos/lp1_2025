#pesquisa utilizando for e enumerate

lista = [8, 4, 7, 5, 2]
numero = int(input("Digite um numero: "))
for indice, valor in enumerate(lista):
    if valor == numero:
        print(f'Achei o {numero} no índice {indice}!')
        break
else:
    print(f'Não achei o {numero}!')