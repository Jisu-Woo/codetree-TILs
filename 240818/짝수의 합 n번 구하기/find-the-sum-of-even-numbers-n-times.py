n = int(input())

for i in range(n):
    z = input().split()
    a, b = int(z[0]), int(z[1])
    sum = 0
    for j in range(a, b + 1):
        if j % 2 == 0:
            sum += j
    print(sum)