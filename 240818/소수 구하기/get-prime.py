n = int(input())

for i in range(2, n + 1):
    is_sosu = True
    for j in range(2, i):
        if i % j == 0:
            is_sosu = False
    if is_sosu:
        print(i, end=" ")