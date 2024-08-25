n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

all_cnt = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            ni = i + dx
            nj = j + dy
            if in_range(ni, nj):
                if arr[ni][nj] == 1:
                    cnt += 1
        if cnt >= 3:
            all_cnt += 1

print(all_cnt)