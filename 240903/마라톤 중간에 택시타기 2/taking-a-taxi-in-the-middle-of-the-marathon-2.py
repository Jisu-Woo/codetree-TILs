n = int(input())
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

min_dist = -1
for i in range(n): # i 는 건너뛸 체크포인트의 인덱스
    if i == 0 or i == n - 1: # 처음과 마지막은 안됨
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
    if min_dist == -1: # 최소 거리 초기 값 할당해주기
        min_dist = dist
    if dist < min_dist:
        min_dist = dist

print(min_dist)