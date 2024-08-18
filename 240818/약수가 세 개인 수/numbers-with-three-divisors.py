z = input().split()
a, b = int(z[0]), int(z[1])

cnt = 0 # 약수가 3개인 수의 개수
for i in range(a, b + 1):
    cnt_yak = 0 # 약수 개수
    for j in range(1, i + 1):
        if i % j == 0:
            cnt_yak += 1
    if cnt_yak == 3:
        cnt += 1

print(cnt)