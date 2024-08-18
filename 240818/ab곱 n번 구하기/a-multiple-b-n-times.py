n = int(input())

for i in range(n):
    z = input().split()
    a, b = int(z[0]), int(z[1])

    result = 1
    for j in range(a, b + 1):
        result *= j
    print(result)