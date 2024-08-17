n = int(input())

cnt = 1

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        if cnt >= 10:
            cnt = 1
        print(cnt, end=" ")
        cnt += 1
    print()