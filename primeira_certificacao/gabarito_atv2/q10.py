#Questão 10 - Extra
i = 1
while i <= 10:
    j = 1
    while j <= 10: # Passa pelos 10 valores de j para cada valor de i do while externo
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1