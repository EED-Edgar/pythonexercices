salario = float(input("Informe seu salário: "))
prestacao = float(input("Informe o valor da prestação: "))

p25 = salario * 0.25

if prestacao > p25:
    print(" Empréstimo não Concedido – Valor Ultrapassa a Margem de Endividamento")
else:
    print("Empréstimo concedido")
