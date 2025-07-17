#Questão 4
PRECO_PAO = 0.12
PRECO_BROA = 1.5
qtd_pao = int(input("Digite a quantidade de pães: "))
qtd_broa = int(input("Digite a quantidade de broas: "))
valorArrecadado = qtd_pao * PRECO_PAO + qtd_broa * PRECO_BROA
print(f"Você arrecadou R${valorArrecadado:.2f}.")
poupanca = valorArrecadado * 0.1
print(f"Você deve guardar R${poupanca:.2f} na poupança.")