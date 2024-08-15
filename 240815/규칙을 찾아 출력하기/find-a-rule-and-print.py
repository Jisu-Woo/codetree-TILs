n = int(input())

# i가 1 일때의 출력
for i in range(n):
    print("*", end=" ")
print()

# i가 1~n-1 줄 까지의 출력
for i in range(1, n):
    for j in range(i):
        print("*", end=" ")
    for j in range(n - i - 1):
        print(" ", end=" ")
    print("*")