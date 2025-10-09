#Questão 7
contador = 1
total = 0  # variável para acumular a soma dos números

while contador <= 4:
    num = float(input(f"Digite o {contador}º número: "))
    total += num
    contador += 1

media = total / 4
print(f"A média aritmética é: {media}")