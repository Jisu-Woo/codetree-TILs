arr = list(map(int, input().split()))

even_arr = arr[1::2]
odd_arr = arr[::2]
even_sum = sum(even_arr)
odd_sum = sum(odd_arr)

if even_sum > odd_sum:
    print(even_sum - odd_sum)
else:
    print(odd_sum - even_sum)