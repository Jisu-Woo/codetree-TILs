n = int(input())

count_up = 1
count_down = n

for i in range(n*2):
    if i % 2 == 0:
        for j in range(count_up):
            print("*", end=" ")
        count_up += 1
    if i % 2 == 1:
        for j in range(count_down):
            print("*", end=" ")
        count_down -= 1
    print()