z = input().split()

a = int(z[0])
b = int(z[1])
c = int(z[2])

if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
else:
    if a > c:
        print(a)
    elif b > c:
        print(c)
    else:
        print(b)