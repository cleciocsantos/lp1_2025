# Versão utilizando o close para fechar o arquivo:
arquivo = open("numeros.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

# Versão utilizando o with (não precisa mais do close):
with open("numeros.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
