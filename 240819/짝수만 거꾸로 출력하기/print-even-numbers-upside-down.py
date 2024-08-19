n = int(input())

arr = list(map(int, input().split()))

list = []

for elem in arr:
    if elem % 2 == 0:
        list.append(elem)

for elem in list[::-1]:
    print(elem, end=" ")