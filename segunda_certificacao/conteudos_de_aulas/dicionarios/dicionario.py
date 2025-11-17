# Um dicionário é composto por um conjunto de chaves e valores.
# Dicionários são definidos com {}, enquanto as listas são definidas com [].
# No dicionário abaixo, "laranja" é uma chave e 2.5 é o valor associado a ela.

tabela = {
    "laranja": 2.5,
    "maçã": 3.15,
    "kiwi": 9.5,
    "amora": 12.0,
    "maxixe": 7.0 # após o último par de chave e valor não usamos a vírgula.
}

# Acessar um valor no dicionário é parecido com acessar um valor numa lista.
# A diferença é que usamos uma chave em vez de um índice entre colchetes.

print(tabela["laranja"]) # essa linha imprime 2.5 na tela

# Para testarmos se uma chave existe num dicionário usamos o operador in.
# O resultado do if abaixo é verdadeiro se "uva" for uma chave do dicionário tabela e falso caso contrário.

if "uva" in tabela:
    print(tabela["uva"])
else:
    print("uva não está na tabela")


# Ao atribuir um valor a uma chave do dicionário, duas situações podem ocorrer:
# Se a chave já existir, o valor que estava associado a ela mudará.
# Se a chave não existir, ela será automaticamente adicionada ao dicionário com o valor atribuído.

tabela["laranja"] = 3.0 # esta linha altera o valor associado à laranja de 2.5 para 3.0.
tabela["uva"] = 8.0 # esta linha cria uma nova chave uva com o valor 8.0.

# O print abaixo imprime o dicionário inteiro na tela.
# Normalmente usado durante o desenvolvimento para verificar se alguma operação produziu o resultado esperado.
print(tabela)