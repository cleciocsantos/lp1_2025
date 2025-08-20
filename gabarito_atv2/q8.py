#Questão 8
contador = 0
total = 0

while True:
    num = int(input("Digite um número inteiro (0 para sair): "))
    if num == 0:
        break # sai imediatamente do while se o número for 0
    contador += 1
    total += num

if contador > 0:
    media = total / contador
else:
    media = 0

print(f"Quantidade de números digitados: {contador}")
print(f"Soma dos números: {total}")
print(f"Média aritmética: {media}")