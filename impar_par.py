#Programa Impar_Par
n1 = int(input("Entre com o número: "))
resto = n1 % 2  # o operador % retorna o resto da divisão de n1 por 2.
if resto:       # se resto tiver qualquer número diferente de zero a condição será verdadeira.
    print(f"O número {n1} é ímpar")
else:
    print(f"O número {n1} é par")