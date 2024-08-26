n, t = tuple(map(int, input().split()))
arr = input().split()
r, c = int(arr[0]), int(arr[1])
d = arr[2]

dx = [0, 1, -1, 0] # 행
dy = [1, 0, 0, -1] # 열

diction = {
    'U' : 2,
    'D' : 1,
    'R' : 0,
    'L' : 3
}

dir_num = diction[d]

def in_range(x, y):
    return x >= 1 and x <= n and y >= 1 and y <= n

sec = 0
while sec < t:
    nx, ny = r + dx[dir_num], c + dy[dir_num]
    if in_range(nx, ny):
        r = nx
        c = ny
        sec += 1
    else:
        dir_num = 3 - dir_num
        sec += 1

print(r, c)