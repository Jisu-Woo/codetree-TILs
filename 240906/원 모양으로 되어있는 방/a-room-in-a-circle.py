n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

min_sum = 0
for i in range(n): # 시작 방 index
    dist_sum = 0
    for j in range(n):
        if j >= i: # 시작 방 index 보다 현재 방 index가 더 큰 경우
            dist_sum += abs(j - i) * arr[j]
        else: # 현재 방 idx가 더 작은 경우 (한바퀴 돌고 가야함)
            dist_sum += (n - abs(j - i)) * arr[j]
    
    if i == 0:
        min_sum = dist_sum
    if dist_sum < min_sum:
        min_sum = dist_sum

print(min_sum)