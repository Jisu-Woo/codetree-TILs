n = int(input())

for i in range(n):
    for j in range(n - 1 - i):
        print(" ", end="")
    for j in range(1 + i*2):
        print("*", end="")
    print()

for i in range(n - 1):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(1 + 2*(n-1) - 2 - i*2):
        print("*", end="")
    print()