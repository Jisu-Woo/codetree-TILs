z = input().split()

a = int(z[0])
b = int(z[1])


while a <= b:
    print(a, end=" ")
    if a % 2 == 0:
        a += 3
    else:
        a *= 2