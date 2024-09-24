arr = ['L', 'E', 'B', 'R', 'O', 'S']

char = input()
idx = -1
if char in arr:
    idx = arr.index(char)

if idx == -1:
    print("None")
else:
    print(idx)