n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

max_ = -1
no_list = []

for elem in arr:
    if elem == max_:
        max_ = -1
        no_list.append(elem)
        continue
    if elem > max_ and elem not in no_list:
        max_ = elem

print(max_)