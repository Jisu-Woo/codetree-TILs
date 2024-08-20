arr= list(map(int, input().split()))

new_arr = []
for elem in arr:
    if elem == 0:
        break
    new_arr.append(elem)

print(new_arr[-1] + new_arr[-2] + new_arr[-3])