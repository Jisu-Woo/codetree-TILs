n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(n - 1):
    for j in range(0, 4 - i):
        print("*", end=" ")
    print()