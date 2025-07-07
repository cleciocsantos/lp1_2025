#Programa Iguais_Diferetes_Versão1 (sem elif)
n1 = int(input("Entre com n1: "))
n2 = int(input("Entre com n2: "))
n3 = int(input("Entre com n3: "))
if n1 == n2 and n1 == n3:
    print("São todos iguais")
if (n1 == n2 and n1 != n3) or (n1 == n3 and n1 != n2) or (n2 == n3 and n2 != n1):
    print("Dois são iguais e um é diferente")
if n1 != n2 and n1 != n3 and n2 != n3:
    print("São todos diferentes")