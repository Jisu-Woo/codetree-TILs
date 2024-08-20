arr = list(map(int, input().split()))

even_arr = arr[1::2]
three_arr = arr[2::3]

print(f"{sum(even_arr)} {sum(three_arr)/3:.1f}")