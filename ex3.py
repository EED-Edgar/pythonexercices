# Faça um programa em python que receba três números e informe qual deles é o menor. Suponha que os números são distintos

a = int(input("Informe três números: "))
b = int(input())
c = int(input())

if a > b and a > c:
    print("o número ",a," é maior que ",b," e ",c)
elif b > a and b > c:
    print("o número ",b," é maior que ",a," e ",c)
else:
    print("o número ",c," é maior que ",a," e ",b)