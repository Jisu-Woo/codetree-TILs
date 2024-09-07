arr = list(input())

open_sum = 0
close_sum = 0
is_open = False
for i in range(len(arr) - 1):
    if arr[i] == "(" and arr[i+1] == "(":
        open_sum += 1
        is_open = True
    if is_open and arr[i] == ")" and arr[i+1] == ")":
        close_sum += 1

print(open_sum * close_sum)