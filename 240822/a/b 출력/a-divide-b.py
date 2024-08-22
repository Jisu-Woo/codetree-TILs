a, b = tuple(map(int, input().split()))

print(a//b, end=".")
k = a % b

for i in range(20):
    k *= 10
    print(k//b, end="")
    k = k % b # 나머지 계속 갱신