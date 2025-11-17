def valida_inteiro(minimo, maximo):
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero >= minimo and numero <= maximo:
                return numero
            else:
                print(f"Valor fora dos limites! Digite um número entre {minimo} e {maximo}")
        except ValueError:
            print(f"Valor inválido! Digite um número inteiro!")

numero = valida_inteiro(30, 40)
print(f"Você digitou {numero}!")

