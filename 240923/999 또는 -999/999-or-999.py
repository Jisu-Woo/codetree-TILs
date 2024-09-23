arr = list(map(int, input().split()))
min_ = 1000
max_ = -1000
for elem in arr:
    if elem == 999 or elem == -999:
        break
    if elem < min_:
        min_ = elem
    elif elem > max_:
        max_ = elem

print(f"{max_} {min_}")