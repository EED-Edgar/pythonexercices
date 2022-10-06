a = int(input("Informe quatro números"))
b = int(input())
c = int(input())
d = int(input())

print("\n")

if a > b and a > c and a > d:
    print(a)
    if b > c and b > d:
        print(b)
        if c > d:
            print(c)
            print(d)
        else:
            print(d)
            print(c)
    elif c > b and c > d:
        print(c)
        if b > d:
            print(b)
            print(d)
        else:
            print(d)
            print(b)
    elif d > b and d > c:
        print(d)
        if b > c:
            print(b)
            print(c)
        else:
            print(c)
            print(b) 

elif b > a and b > c:
    print(b)
    if a > c and a > d:
        print(a)
        if c > d:
            print(c)
            print(d)
        else:
            print(d)
            print(c)
    elif c > a and c > d:
        print(c)
        if a > d:
            print(a)
            print(d)
        else:
            print(d)
            print(a)
    elif d > a and d > c:
        print(d)
        if a > c:
            print(a)
            print(c)
        else:
            print(c)
            print(a)

elif c > a and c > b:
    print(c)
    if a > b and a > d:
        print(a)
        if b > d:
            print(b)
            print(d)
        else:
            print(d)
            print(b)
    elif b > a and b > d:
        print(b)
        if a > d:
            print(a)
            print(d)
        else:
            print(d)
            print(a)
    elif d > a and d > b:
        print(d)
        if a > b:
            print(a)
            print(b)
        else:
            print(b)
            print(a)
elif d > a and d > b and d > c:
    print(d)
    if a > b and a > c:
        print(a)
        if b > c:
            print(b)
            print(c)
        else:
            print(c)
            print(b)
    elif b > a and b > c:
        print(b)
        if a > c:
            print(a)
            print(c)
        else:
            print(c)
            print(a)
    elif c > a and c > b:
        print(c)
        if a > b:
            print(a)
            print(b)
        else:
            print(b)
            print(a)