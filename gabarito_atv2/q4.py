#Questão 4
n = int(input("Digite um número para a contagem regressiva: "))
while n >= 0:
    print(n)
    n -= 1 # a cada rodada o número diminui em 1
print("Terminei!") # este print só é executado após o while terminar.