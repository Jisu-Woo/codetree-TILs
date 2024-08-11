z = input().split()

a = int(z[0])
b = int(z[1])

sum = 0
for i in range(a, b + 1):
    if i % 6 == 0 and i % 8 != 0:
        sum += i

print(sum)