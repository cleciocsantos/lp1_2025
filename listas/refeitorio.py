alunos = []
while True:
    print(f"Existem {len(alunos)} alunos na fila.")
    print("Digite uma das opções:\n "
          "F - para adicionar um aluno no fim da fila.\n "
          "A - para atender o primeiro da fila.\n "
          "S - para sair.")
    opcao = input("Operação (F, A ou S): ")
    if opcao.lower() == 's':
        break
    elif opcao.lower() == 'f':
        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)
    elif opcao.lower() == 'a':
        if len(alunos) > 0:
            nome = alunos.pop(0)
            print(f"O aluno {nome} foi atendido")
        else:
            print("A lista está vazia!")
    else:
        print(f"Opção {opcao} inválida! Escolha F, A ou S!")


