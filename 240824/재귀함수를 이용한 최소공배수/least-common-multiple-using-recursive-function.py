n = int(input())

arr = list(map(int, input().split()))

for i in range(1, 10000):
    is_True = True
    for j in range(n):
        if i % arr[j] != 0:
            is_True = False
    if is_True:
        print(i)
        break