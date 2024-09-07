arr = list(input())

open_pos = [] # 열리는 쌍의 위치를 저장
close_pos = [] # 닫히는 쌍의 위치를 저장
cnt = 0
for i in range(len(arr) - 1):
    if arr[i] == "(" and arr[i+1] == "(":
        open_pos.append(i)

for i in range(len(arr) - 1):
    if arr[i] == ")" and arr[i+1] == ")":
        close_pos.append(i)

for i in open_pos:
    for j in close_pos:
        if i < j:
            cnt += 1

print(cnt)