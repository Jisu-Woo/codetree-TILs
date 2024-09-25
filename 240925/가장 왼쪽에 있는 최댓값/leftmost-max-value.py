n = int(input())

arr = list(map(int, input().split()))

max_ = -1
idx = -1
is_Finish = False
while not is_Finish:
    max_ = -1
    idx = -1
    for i in range(n):
    
        if arr[i] > max_:
            max_ = arr[i]
            idx = i + 1

    print(idx, end=" ")
        
    if idx == 1:
        is_Finish = True
        break
    n = idx - 1