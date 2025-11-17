def maximo(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

def multiplo(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

def area_quadrado(lado):
    area = lado ** 2
    return area

def area_trinagulo(base, altura):
    area = (base * altura) / 2
    return area

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"O maior número entre {a} e {b} é {maximo(a,b)}")

if multiplo(a,b):
    print(f"{a} é múltiplo de {b}")
else:
    print(f"{a} NÃO é múltiplo de {b}")