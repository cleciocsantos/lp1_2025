print("Olá! Seja bem-vindo ao sistema da DS102!")

# Preenchimento da lista de alunos
alunos = []
while True:
    nome = input("Digite o nome de um aluno ou fim para sair: ")
    if nome.lower() == "fim":
        break
    alunos.append(nome)

# Exibição em letra maiúscula dos itens da lista
x = 0
while x < len(alunos):
    print(alunos[x].upper())
    x += 1

# Exibição dos itens da lista usando for
for aluno in alunos:
    print(aluno)