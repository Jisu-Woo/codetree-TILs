import sys

n = int(input())
arr = list(map(int, input().split()))

min_ = sys.maxsize
cnt = 0

for elem in arr:
    if elem < min_:
        min_ = elem
        cnt = 1
    elif elem == min_:
        cnt += 1

print(f"{min_} {cnt}")