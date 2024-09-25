n1, n2 = tuple(map(int, input().split()))
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

idx = 1
okay = True
isFinished = False
for i in range(len(arr_a)):
    idx = 1
    okay = True
    if arr_a[i] == arr_b[0] and len(arr_b) + i <= len(arr_a):
        for j in range(i + 1, i + len(arr_b)):
            if arr_a[j] != arr_b[idx]:
                okay = False
                break
                
            elif arr_a[j] == arr_b[idx]:
                idx += 1
        if okay:
            print("Yes")
            isFinished = True
            break

if not isFinished:
    print("No")