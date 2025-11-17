produto1 = ["maçã", 10, 0.30]
produto2 = ["laranja", 5, 0.75]
produto3 = ["uva", 4, 0.98]
compras = [produto1, produto2, produto3] # Essa lista contém outras listas como seus elementos

print(compras) # esse print retorna: [['maçã', 10, 0.3], ['laranja', 5, 0.75], ['uva', 4, 0.98]]
print(compras[1]) # esse print retorna: ['laranja', 5, 0.75]
print(compras[1][0]) # esse print retorna: laranja

# comando for para listar nome, quantidade e preço de todos os produtos da lista de compras
for produto in compras:
    print(f"Nome: {produto[0]}")
    print(f"Quantidade: {produto[1]}")
    print(f"Preço: {produto[2]}")

# comando while para listar nome, quantidade e preço de todos os produtos da lista de compras
x = 0
while x < len(compras):
    print(f"Nome: {compras[x][0]}")
    print(f"Quantidade: {compras[x][1]}")
    print(f"Preço: {compras[x][2]}")
    x += 1