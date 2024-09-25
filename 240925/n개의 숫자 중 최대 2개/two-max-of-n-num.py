n = int(input())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

print(f"{arr[0]} {arr[1]}")