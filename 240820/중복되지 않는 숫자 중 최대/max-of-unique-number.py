n = int(input())

arr = list(map(int, input().split()))
check_arr = []
for elem in arr:
    if elem in check_arr:
        check_arr.remove(elem)
    else:
        check_arr.append(elem)

check_arr.sort()
print(check_arr[-1])