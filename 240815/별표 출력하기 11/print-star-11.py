n = int(input())

for i in range(1 + 2*n):
    if i % 2 == 0:
        for j in range(1 + 2*n):
            print("*", end=" ")
        print()
    else:
        for j in range(n + 1):
            print("*", end="   ")
        print()