#Questão 9
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    print(f"O preço do produto é R$10,00.")
elif categoria == 2:
    print(f"O preço do produto é R$18,00.")
elif categoria == 3:
    print(f"O preço do produto é R$23,00.")
elif categoria == 4:
    print(f"O preço do produto é R$26,00.")
elif categoria == 5:
    print(f"O preço do produto é R$31,00.")
else:
    print(f"Categoria inválida")