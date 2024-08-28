n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if i < j and j < k:
                if arr[i] <= arr[j] and arr[j] <= arr[k]:
                    cnt += 1

print(cnt)
$0