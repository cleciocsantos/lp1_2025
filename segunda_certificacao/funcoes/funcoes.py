# Exemplo de definição de função sem retorno
def soma(a, b):
    print(a + b)

soma(2, 9)
soma(7, 8)

# Exemplo de definição de função com retorno
def soma2(a, b):
    return a + b

resultado = 5 * soma2(4,9)
print(resultado)

# Exemplo de função com retorno de string
def boasvindas(nome):
    return f"Bem-vindo(a), {nome}!"

print(boasvindas("João"))
print(boasvindas("Maria"))

# Exemplo de função com retorno de valor booleano (Verdadeiro ou Falso)
def épar(x):
    return x % 2 == 0

print(épar(6))
print(épar(7))

# Exemplo de função que chama outra função que criamos
def par_ou_impar(x):
    if épar(x):
        return "par"
    else:
        return "ímpar"

print(par_ou_impar(5))
print(par_ou_impar(8))
