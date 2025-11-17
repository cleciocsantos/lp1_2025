def fatorial(n):
    if n == 0 or n == 1:
        return 1
    fat = n
    n-= 1
    while n > 0:
        fat = fat * n
        n -= 1
    return fat

x = 0
while x < 5:
    numero = int(input("Digite um número: "))
    print(f"O fatorial de {numero} é {fatorial(numero)}")
    x += 1