is_3 = True

for i in range(5):
    n = int(input())
    
    if n % 3 != 0:
        is_3 = False
    
if is_3:
    print(1)
else:
    print(0)