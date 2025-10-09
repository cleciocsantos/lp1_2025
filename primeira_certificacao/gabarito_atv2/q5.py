#Questão 5
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1

x = menor # x recebe o valor do menor, seja ele o num1 ou num2
while x <= maior: # x vai aumentar até o valor do maior, seja ele o num1 ou num2
    print(x)
    x += 1