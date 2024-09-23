arr = list(map(int, input().split()))

max_ = 0

for elem in arr:
    if elem > max_:
        max_ = elem

print(max_)