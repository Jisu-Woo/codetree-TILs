z = input().split()

a = int(z[0])
b = int(z[1])

sum = 0

if a < b:
    for i in range(a, b + 1):
        if i % 5 == 0:
            sum += i
else:
    for i in range(b, a + 1):
        if i % 5 == 0:
            sum += i

print(sum)