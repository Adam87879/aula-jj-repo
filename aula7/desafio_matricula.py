def verificar_grupo (matricula):
    if matricula % 2 == 0:
        print("você está no time azul")
    elif matricula > 100:
        print("aluno não reconhecido")
    else:
        print("você está no time amarelo")
matricula = int(input("digite seu numeroda matricula aqui: "))

verificar_grupo(matricula)