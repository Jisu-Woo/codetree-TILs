z = input().split()

a = int(z[0])
b = int(z[1])
c = int(z[2])

is_exist = False
for i in range(a, b + 1):
    if i % c == 0:
        is_exist = True
    

if is_exist:
    print('YES')
else:
    print('NO')