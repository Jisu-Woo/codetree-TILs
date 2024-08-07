z = input().split()

a = int(z[0])
b = int(z[1])
c = int(z[2])

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)