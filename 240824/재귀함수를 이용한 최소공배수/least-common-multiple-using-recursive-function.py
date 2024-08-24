n = int(input())

arr = list(map(int, input().split()))

def ret(i, j):
    if j >= n:
        return True
    if i % arr[j] == 0:
        return ret(i, j + 1)
    else:
        return False




for i in range(1, 10000):
    is_True = ret(i, 0)
    #for j in range(n):
    #    ret(i, 0)
    #    if i % arr[j] != 0:
    #        is_True = False
    if is_True:
        print(i)
        break