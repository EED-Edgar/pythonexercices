nota = int(input("Qual a nota do aluno? "))

if nota >= 70:
    print("Aprovado")
elif nota >= 60 and nota < 70:
    print("Em exame")
else:
    print("Reprovado")