#Questão 8
salario = int(input("Digite o salário: "))
if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15
print(f"O aumento foi de R${aumento:.2f}.")