n = int(input())
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

max_cnt = 0
for i in range(n):
    for j in range(n - 2):
        sum_cnt = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        if sum_cnt > max_cnt:
            max_cnt = sum_cnt

print(max_cnt)