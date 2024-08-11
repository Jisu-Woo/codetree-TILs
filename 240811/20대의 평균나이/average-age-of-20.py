sum = 0
cnt = 0
while True:
    n = int(input())
    
    if n >= 30 or n < 20:
        print(f"{sum/cnt:.2f}")
        break
    else:
        sum += n
        cnt += 1