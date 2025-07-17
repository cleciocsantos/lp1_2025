#Questão 7
velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado! Pague R${multa:.2f} de multa.")
