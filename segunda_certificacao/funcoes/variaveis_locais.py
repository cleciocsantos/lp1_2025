a = 5
def muda_e_imprime():
    a = 7 # só existe dentro da função, não alterando o valor de a fora da função.
    print(f"A dentro da função: {a}")

print(f"A antes de mudar: {a}")
muda_e_imprime()
print(f"A depois de mudar: {a}")

a = 5
def muda_e_imprime():
    global a # a palavra 'global' é usada para modificar variáveis que foram criadas fora da função.
    a = 7
    print(f"A dentro da função: {a}")

print(f"A antes de mudar: {a}")
muda_e_imprime()
print(f"A depois de mudar: {a}")