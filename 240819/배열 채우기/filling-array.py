arr = []

list = list(map(int, input().split()))

for elem in list:
    if elem == 0:
        break
    arr.append(elem)

for elem in arr[::-1]:
    print(elem, end=" ")