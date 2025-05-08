from collections import deque

N, T = map(int, input().split())
F = []
B = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    line = list(input())
    F.append(line)

for i in range(N):
    line = list(map(int, input().split()))
    B.append(line)

def get_groups(x, y, groups, visited):

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    group = []
    group.append([x, y])
    food = F[x][y]

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]

            # 맵 안에 존재하고, 방문 전이고, 같은 음식이라면 그룹화
            if 0 <= na < N and 0 <= nb < N and visited[na][nb] == 0 and F[na][nb] == food:
                queue.append((na, nb))
                visited[na][nb] = 1
                group.append([na, nb])
        
    groups.append(group)

    return

def get_head(group):
    group.sort(key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))

    head_x, head_y = group[0]
    return head_x, head_y

def food_sum(food1, food2):
    f1 = list(food1)
    f2 = list(food2)

    f1_set = set(f1)
    f2_set = set(f2)

    f1_set.update(f2_set)
    f1_list = list(f1_set)
    f1_list.sort() # 항상 같은 순서로 반환하도록

    return ''.join(f1_list)

def shooting(head, dependers):
    h_x, h_y = head
    food = F[h_x][h_y]
    
    #dependers.add((h_x, h_y))
    d = B[h_x][h_y] % 4
    # 간절함 x   
    x = B[h_x][h_y] - 1

    B[h_x][h_y] = 1

    nx, ny = h_x + dx[d], h_y + dy[d]
    while 0 <= nx < N and 0 <= ny < N and x > 0:
        
        # 서로 다를 경우만 전파
        if food != F[nx][ny]:
            y = B[nx][ny]
            # 강한 전파
            if x > y:
                F[nx][ny] = food
                x -= y + 1
                B[nx][ny] += 1
            # 약한 전파
            else:
                sum_food = food_sum(food, F[nx][ny])
                
                F[nx][ny] = sum_food
                B[nx][ny] += x
                x = 0
            dependers.add((nx, ny))

        # 방향으로 한 칸 이동
        nx += dx[d]
        ny += dy[d]

    return



for i in range(T):

    # 아침
    for j in range(N):
        for k in range(N):
            B[j][k] += 1

    # 점심
    groups = []

    # 그룹 형성하기
    visited =[[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if visited[j][k] == 0:
                get_groups(j, k, groups, visited)
    # 그룹 내 대표자 선정하기
    heads = []
    
    for group in groups:
        h_x, h_y = get_head(group)
        heads.append((h_x, h_y))
    
    # 대표자에게 신앙심 1씩 넘기기
    for idx in range(len(groups)):
        group = groups[idx]
        head = heads[idx]

        for x, y in group:
            # 대표자 빼고
            if x == head[0] and y == head[1]:
                continue
            # 그룹원들 1씩 감소
            #if B[x][y] >= 0: # ?
            B[x][y] -= 1
        # 대표자 신앙심 추가
        B[head[0]][head[1]] += len(group) - 1
    

    # 저녁
    f1_heads = []
    f2_heads = []
    f3_heads = []
    for head in heads:
        h_x, h_y = head[0], head[1]
        if len(F[h_x][h_y]) == 1:
            f1_heads.append(head)
        elif len(F[h_x][h_y]) == 2:
            f2_heads.append(head)
        else:
            f3_heads.append(head)
    
    f1_heads.sort(key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))
    f2_heads.sort(key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))
    f3_heads.sort(key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))
    
    dependers = set()

    # f1_head 신앙 전파
    for head in f1_heads:
        if head not in dependers:
            shooting(head, dependers)
    # f2_head 신앙 전파
    for head in f2_heads:
        if head not in dependers:
            shooting(head, dependers)
    # f3_head 신앙 전파
    for head in f3_heads:
        if head not in dependers:
            shooting(head, dependers)
    
    #print(dependers)

    mcw = 0
    mc = 0
    mw = 0
    cw = 0
    w = 0
    c = 0
    m = 0
    # 신앙심 총합 출력
    for j in range(N):
        for k in range(N):
            food = F[j][k]
            power = B[j][k]
            if 'M' in food and 'C' in food and 'T' in food:
                mcw += power
            elif 'M' in food and 'C' in food:
                cw += power
            elif 'M' in food and 'T' in food:
                mw += power
            elif 'C' in food and 'T' in food:
                mc += power
            elif 'M' in food:
                w += power
            elif 'C' in food:
                c += power
            elif 'T' in food:
                m += power
    print(mcw, mc, mw, cw, w, c, m)
