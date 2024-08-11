z = input().split()

a = int(z[0])
b = int(z[1])

sum = 0
cnt = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        cnt += 1

print(f"{sum} {sum/cnt:.1f}")