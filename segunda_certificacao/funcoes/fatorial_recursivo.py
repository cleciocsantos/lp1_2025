'''
Quando uma função faz uma chamada a ela mesma, dizemos que é uma função recursiva.

Abaixo, temos uma versão recursiva da função que calcula o fatorial de um número.
Vemos que o código é mais simples do que a versão não recursiva da função.
Para entender melhor o funcionamento das chamadas recursivas, colocamos prints dentro da função.
'''

def fatorial(n):
    print(f"Calculando o fatorial de {n}")
    if n == 0 or n == 1:
        print(f"Retornando o fatorial de {n}")
        return 1
    fat = n * fatorial(n-1)
    print(f"Retornando o fatorial de {n}")
    return fat

x = 0
while x < 5:
    numero = int(input("Digite um número: "))
    print(f"O fatorial de {numero} é {fatorial(numero)}")
    x += 1