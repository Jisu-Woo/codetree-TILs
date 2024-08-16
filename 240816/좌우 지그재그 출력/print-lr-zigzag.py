n = int(input())

cnt = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(1 + n*i + j, end=" ")
    else:
        for j in range(n):
            print(n*(1 + 1) - j, end=" ")
    print()

#짝수 행 : 1 + n*i 시작값    + 1 씩 반복
#홀수 행 : n * (i+1) 시작값  -1 씩 반복