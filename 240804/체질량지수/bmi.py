z = input().split()

a = int(z[0])
b = int(z[1])

k = (10000*b) / (a*a)
k = int(k)
print(k)
if k >=25:
    print("Obesity")