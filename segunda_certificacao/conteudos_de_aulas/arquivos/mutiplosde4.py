with open("pares.txt") as pares, open("m4.txt", "w") as mDe4:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                mDe4.write(f"{linha}\n")