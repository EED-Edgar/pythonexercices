a = int(input("Informe um número: "))

mod = a % 3
mod2 = a % 5

if mod == 0 and mod2 != 0:
    print(a,"é multiplo de 3")
else:
    print(a,"não é multiplo de 3")
if mod2 == 0 and mod != 0:
    print(a,"É multiplo de 5")
else:
    print(a,"não é multiplo de 5")