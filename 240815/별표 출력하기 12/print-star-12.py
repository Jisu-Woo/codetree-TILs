n = int(input())


for i in range(n):
    print("*", end=" ")
print()

for i in range(1, n + 1):
    for j in range(n):
        if i <= j and j % 2 == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#j == 짝수면 1개
#j == 홀수면 2의 배수