n = int(input())

div_sum = 0

for i in range(1, n):
    if n % i == 0:
        div_sum += i

if div_sum == n:
    print('P')
else:
    print('N')