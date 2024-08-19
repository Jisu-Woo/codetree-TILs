list = list(map(int, input().split()))

cnt = 0
sum = 0
for elem in list:
    if elem == 0:
        break
    elif elem % 2 == 0:
        cnt += 1
        sum += elem

print(cnt, sum)