lugares_vagos = [10, 2, 1,3, 0]

while True:
    print('LISTA DE SALAS')
    for indice, lugares in enumerate(lugares_vagos):
        print(f'Sala {indice + 1}: {lugares} lugares vagos')
    sala = int(input("Digite o número da sala: "))
    if sala == 0:
        break
    elif sala < 0 or sala > 5:
        print('Sala inexistente!')
    else:
        qtdLugares = int(input("Digite o número de lugares solicitados: "))
        if qtdLugares < 0:
            print("Por favor, digite um número positivo.")
        elif lugares_vagos[sala - 1] >= qtdLugares:
            lugares_vagos[sala - 1] -= qtdLugares
            print("Seus lugares foram reservados!")
        else:
            print("Não há lugares suficientes!")
print("Obrigado pela preferência. Volte sempre!")