arquivo = open("numeros.txt", "w")
for linha in range(1, 11):
    arquivo.write(f"Linha: {linha}\n")
arquivo.close()