n, q = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(arr[query[1] - 1])
    elif query[0] == 2:
        idx = 0
        idx = arr.index(query[1]) + 1
        print(idx)
    elif query[0] == 3:
        str_ = ''
        for elem in arr[query[1]-1 : query[2]]:
            str_ += str(elem) + ' '
        print(str_)