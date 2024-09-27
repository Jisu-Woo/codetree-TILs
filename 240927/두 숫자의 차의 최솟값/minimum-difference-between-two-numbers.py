n = int(input())
arr = list(map(int, input().split()))

min_ = 100

for i in range(n - 1):
    if arr[i + 1] - arr[i] < min_:
        min_ = arr[i + 1] - arr[i]

print(min_)