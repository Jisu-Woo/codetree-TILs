z = input().split()
a, b = int(z[0]), int(z[1])

cnt = 0 # 완전수 갯수 변수
for i in range(a, b + 1):
    sum = 0 # 진약수의 총합 변수
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i: # 완전수 카운팅
        cnt += 1

print(cnt)