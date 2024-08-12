z = input().split()

a = int(z[0])
b = int(z[1])

is_exist = False
for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        is_exist = True
    
if is_exist:
    print(1)
else:
    print(0)