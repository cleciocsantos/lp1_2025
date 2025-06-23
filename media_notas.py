#Programa Média_Notas
nome = input("Digite o seu nome: ")
disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3)/3
print(f"{nome}, sua média na disciplina {disciplina} foi {media:.1f}")
