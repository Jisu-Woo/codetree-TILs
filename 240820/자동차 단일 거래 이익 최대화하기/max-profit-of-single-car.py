n = int(input())

arr = list(map(int, input().split()))
benefit_arr = []

low = arr[0]
for i in range(1, n):
    if arr[i] > low:
        benefit_arr.append(arr[i] - low)
    elif arr[i] < low:
        low = arr[i]

if len(benefit_arr) == 0:
    print(0)
else:
    benefit_arr.sort()
    print(benefit_arr[-1])