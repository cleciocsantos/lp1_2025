nomes = ["Maria", "Hermenegildo", "Ypsulon"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except IndexError:
        print("Valor inválido. digite entre -3 e 2")
    except ValueError:
        print("Digite um número inteiro!")