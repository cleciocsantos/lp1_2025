#Programa Iguais_Diferetes_Versão2 (com elif)
n1 = int(input("Entre com n1: "))
n2 = int(input("Entre com n2: "))
n3 = int(input("Entre com n3: "))
if n1 == n2 and n1 == n3:
    print("São todos iguais")
elif n1 == n2  or n1 == n3 or n2 == n3:
    print("Dois são iguais e um é diferente")
else:
    print("São todos diferentes")