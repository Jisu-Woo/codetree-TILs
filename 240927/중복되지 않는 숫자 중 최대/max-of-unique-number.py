n = int(input())
arr = list(map(int, input().split()))

max_ = -1

for elem in arr:
    if elem == max_:
        max_ = -1
        continue
    if elem > max_:
        max_ = elem

print(max_)