#Questão 2
preco_gas = float(input("Digite o preço da gasolina: "))
valor_pagto = float(input("Digite o valor da pagamento: "))
litros = valor_pagto / preco_gas
print(f"Você conseguiu abastecer {litros:.1f} litros.")