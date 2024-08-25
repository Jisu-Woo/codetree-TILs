x, y = 0, 0
dir = 3
str = input()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(len(str)):
    if str[i] == 'L':
        dir = (dir + 3) % 4
    elif str[i] == 'R':
        dir = (dir + 1) % 4
    else:
        x, y = x + dx[dir], y + dy[dir]
        
print(x, y)