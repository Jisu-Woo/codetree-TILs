a = input().split()
b = input().split()

a1 = int(a[0])
a2 = int(a[1])

b1 = int(b[0])
b2 = int(b[1])

if a1 > b1:
    print('A')
elif b1 > a1:
    print('B')
elif a2 > b2:
    print('A')
else:
    print('B')