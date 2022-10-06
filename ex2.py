#Faça um programa em python que verifique se um número é par ou impar.

a = int(input("Informe um número: "))

div2 = a % 2

if div2 == 0:
    print(a," é um número par")
else:
    print(a," é um número impar")