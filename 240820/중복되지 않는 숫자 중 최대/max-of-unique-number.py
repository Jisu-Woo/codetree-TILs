n = int(input())

arr = input().split()

check_arr = []
remove_arr = []
for elem in arr:
    if elem in check_arr:
        check_arr.remove(elem)
        remove_arr.append(elem)
    elif elem in remove_arr:
        continue
    else:
        check_arr.append(elem)
        
if len(check_arr) == 0:
    print(-1)
else:
    check_arr.sort()
    print(check_arr[-1])