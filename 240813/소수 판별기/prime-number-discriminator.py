n = int(input())

is_sosu = True
for i in range(2, n):
    if n % i == 0:
        is_sosu = False

if is_sosu:
    print("P")
else:
    print("C")