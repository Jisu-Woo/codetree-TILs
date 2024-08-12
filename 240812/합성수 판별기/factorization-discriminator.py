n = int(input())

is_num = False
for i in range(2, n):
    if n % i == 0:
        is_num = True

if is_num:
    print('C')
else:
    print('N')