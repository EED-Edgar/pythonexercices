from re import I


a = int(input("Informe um número: "))
i = 0
cont = 0

for i in range(2, a):
    mod = a % i
    if mod == 0:
        cont += 1
if cont == 0 and a >= 2:
    print("É primo")
else:
    print("Não é parente")