z = input().split()

a = int(z[0])
b = int(z[1])
c = int(z[2])

if a <= b and a <= c:
    print(1, end = " ")
else:
    print(0, end = " ")

if a == b and b == c:
    print(1)
else:
    print(0)