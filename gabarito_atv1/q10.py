#Questão 10

#Entrada
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("Números de operação:")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")
num_op = int(input("Digite o número da operação: "))

#Processamento
if num_op == 1:
    opEscolhida = "adição"
    resultado = n1 + n2
elif num_op == 2:
    opEscolhida = "subtração"
    resultado = n1 - n2
elif num_op == 3:
    opEscolhida = "multiplicação"
    resultado = n1 * n2
elif num_op == 4:
    opEscolhida = "divisão"
    resultado = n1 / n2

#Saída
print(f"O resultado da operação {opEscolhida} é {resultado:.1f}")