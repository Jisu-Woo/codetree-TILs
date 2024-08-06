z = input().split()

a = int(z[0])
b = int(z[1])
c = int(z[2])

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)