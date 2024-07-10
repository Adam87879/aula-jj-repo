nome = input("Digite o nome do aluno: ")
n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")
n3 = input("Digite a terceira nota: ")
n4 = input("Digite a quarta nota: ")

nota1 = float(n1)
nota2 = float(n2)
nota3 = float(n3)
nota4 = float(n4)

soma = nota1 + nota2 + nota3 + nota4
media = soma/4

print(f"Olá, {nome}! Sua média é: {media} pontos")