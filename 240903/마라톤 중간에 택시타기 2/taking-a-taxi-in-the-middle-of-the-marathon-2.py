n = int(input())
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

min_dist = 100000
for i in range(n):
    if i == 0 or i == n - 1:
        continue
    dist = 0
    j = 0
    while j <= n - 2:
        if j + 1 == i : # 건너뛸 체크포인트
            dist += abs(arr[j + 2][0] - arr[j][0]) + abs(arr[j + 2][1] - arr[j][1])
            j += 2
        else:
            dist += abs(arr[j + 1][0] - arr[j][0]) + abs(arr[j + 1][1] - arr[j][1])
            j += 1
    if dist < min_dist:
        min_dist = dist

print(min_dist)