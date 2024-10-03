n, m = tuple(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if j == 0:
            print(i, end=" ")
            num = i
        elif j % 2 == 1:
            num = num + n*2 - 1 - i*2
            print(num, end=" ")
        elif j % 2 == 0:
            num = num + 1 + i*2
            print(num, end=" ")
    print()