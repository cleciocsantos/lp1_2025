#Questão 6
contador = 1
produto = 1 # inicializando o produto com 1, pois é o elemento neutro da multiplicação

while contador <= 5:
    num = float(input(f"Digite o {contador}º número: "))
    produto *= num # multiplicando o número atual pelo produto anterior
    contador += 1

print("O resultado da multiplicação é:", produto)