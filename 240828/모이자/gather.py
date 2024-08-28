n = int(input())

arr = list(map(int, input().split()))

min = 1000
for i in range(len(arr)):
    total = 0
    for j in range(len(arr)):
        total += arr[j] * abs(j - i)
    if min > total:
        min = total

print(min)