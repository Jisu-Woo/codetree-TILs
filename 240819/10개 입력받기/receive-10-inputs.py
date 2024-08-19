list = list(map(int, input().split()))

sum = 0
cnt = 0
for elem in list:
    if elem == 0:
        break
    sum += elem
    cnt += 1

print(f"{sum} {sum/cnt:.1f}")