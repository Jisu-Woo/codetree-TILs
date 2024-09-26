arr = list(map(int, input().split()))

max_ = 0
min_ = 1001

for elem in arr:
    if elem < 500 and elem > max_:
        max_ = elem
    elif elem > 500 and elem < min_:
        min_ = elem
    

print(max_, min_)