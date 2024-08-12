n = int(input())

cnt = 0
while True:
    if n == 1:
        print(cnt)
        break
    else:
        n //= 2
        cnt += 1