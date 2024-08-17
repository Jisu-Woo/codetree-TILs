z = input().split()
a = int(z[0])
b = int(z[1])

for i in range(1, 10):
    for j in range(b, a - 1, -2):
        print(f"{j} * {i} = {i*j}", end=" ")

        if j > a:
            print("/", end=" ")
    print()