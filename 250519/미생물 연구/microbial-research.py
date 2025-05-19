from collections import deque
import copy

n, q = map(int, input().split())

pos = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

pos.append([0])  # 인덱스 1부터로 맞추기 위함

for i in range(q):
    line = list(map(int, input().split()))
    pos.append(line)

maps = [[0] * n for _ in range(n)]


def bfs(x, y, visited, idx):

    queue = deque()
    queue.append((x, y))
    visited.append([x, y])  # 방문 처리

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (
                0 <= nx < n
                and 0 <= ny < n
                and [nx, ny] not in visited
                and maps[nx][ny] == idx
            ):
                queue.append((nx, ny))
                visited.append([nx, ny])  # 방문 처리

    return


def count_size(x, y, visited, idx):
    queue = deque()
    queue.append((x, y))
    visited.append([x, y])  # 방문 처리
    size = 1

    coord_list = []
    coord_list.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (
                0 <= nx < n
                and 0 <= ny < n
                and [nx, ny] not in visited
                and maps[nx][ny] == idx
            ):
                queue.append((nx, ny))
                visited.append([nx, ny])  # 방문 처리
                coord_list.append([nx, ny])
                size += 1

    return size, coord_list


def check_neighbor(x, y, visited, idx, neighbor_list):

    queue = deque()
    queue.append((x, y))
    visited.append([x, y])  # 방문 처리

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (
                0 <= nx < n
                and 0 <= ny < n
                and [nx, ny] not in visited
                and new_maps[nx][ny] == idx
            ):
                queue.append((nx, ny))
                visited.append([nx, ny])  # 방문 처리
            elif (
                0 <= nx < n
                and 0 <= ny < n
                and [nx, ny] not in visited
                and new_maps[nx][ny] != 0
                and new_maps[nx][ny] != idx
                and new_maps[nx][ny] not in neighbor_list
            ):
                neighbor_list.add(frozenset([idx, new_maps[nx][ny]]))


def get_size(idx, sizes):
    for size in sizes:
        if size[0] == idx:
            return size[1]
    return -1


# 총 q번의 실험 진행
# for i in range(q):

# 1) 미생물 투입
for j in range(1, len(pos)):
    r1, c1, r2, c2 = pos[j]

    for x in range(r1, r2):
        for y in range(c1, c2):
            maps[x][y] = j  # 미생물 무리의 인덱스로 표시

    #print("투입 완료 삭제 전")
    #for z in range(0, n):
    #    print(maps[z])
    # 무리 하나 투입할 때마다 다른 무리가 둘 이상으로 나눠졌다면 나눠진 무리는 모두 삭제
    # 확인 방법: 현재 투입된 무리보다 먼저 투입된 모든 무리들의 (r1, c1) 부터 (r2, c2) 까지 훑으면서 특정 좌표에서 해당 인덱스를 발견 시
    # 그 좌표로 bfs 진행 -> 방문처리하기
    # 다시 나머지 좌표 훑으면서 방문하지 않은 좌표 중에서 해당 인덱스를 또 발견한다면 둘 이상으로 쪼개진 것 -> 모두 삭제
    for idx in range(1, j):
        # r1_, c1_, r2_, c2_ = pos[idx]

        visited = []
        already_found = False

        for x in range(0, n):
            for y in range(0, n):
                if maps[x][y] == idx and [x, y] not in visited:  # 현재 무리 인덱스 발견
                    if already_found:
                        # 모두 삭제
                        # (r1, c1) ~ (r2, c2)를 돌면서 해당 인덱스 0으로 초기화
                        for a in range(0, n):
                            for b in range(0, n):
                                if maps[a][b] == idx:
                                    maps[a][b] = 0
                    else:
                        bfs(x, y, visited, idx)
                        already_found = True

    #print("이동 전")
    #for z in range(0, n):
    #    print(maps[z])
    # 배양 용기 이동
    # 순서: 가장 넓은 무리(중에서도 먼저 투입된 무리) 순
    # 전체 돌면서 각 무리의 칸 수 카운트하기
    sizes = []
    visited = []
    coords = {}

    for x in range(0, n):
        for y in range(0, n):
            if maps[x][y] != 0 and [x, y] not in visited:
                idx = maps[x][y]

                s, coord_list = count_size(x, y, visited, idx)
                coords[idx] = coord_list
                sizes.append([idx, s])

    # 무리 중 가장 넓은 무리 순(내림차순), 그다음엔 먼저 투입된 무리(오름차순) 순으로 정렬
    sizes.sort(key=lambda x: (-x[1], x[0]))

    # print(sizes)
    # 새로운 맵에 옮기기 ----------------------------

    new_maps = [[0] * n for _ in range(n)]

    for idx, size in sizes:
        coord_list = coords.get(idx)

        coord_list.sort(key=lambda x: x[0])
        min_x = coord_list[0][0]
        coord_list.sort(key=lambda x: x[1])
        min_y = coord_list[0][1]

        # print(idx, min_x, min_y)
        # print(idx, "의 ", coord_list)

        is_done = False  # 이번 idx의 미생물을 배치 완료했다면 True

        for x in range(0, n):
            for y in range(0, n):
                # print("탐색 ", x, y)
                # if new_maps[x][y] == 0:  # 빈 공간을 찾았다면
                # print("여기부터 시작: ", x, y)
                # 현재 미생물이 들어갈 수 있는 공간이 되는지 체크
                is_possible = True

                for coord in coord_list:
                    a = coord[0]
                    b = coord[1]

                    nx = x + a - min_x
                    ny = y + b - min_y
                    if 0 > nx or nx >= n or 0 > ny or ny >= n:
                        is_possible = False
                        break
                    elif new_maps[nx][ny] != 0:
                        is_possible = False
                        break

                # 해당 x, y 좌표에 미생물 들어갈 자리가 된다면 옮기기
                if is_possible:
                    for coord in coord_list:
                        a = coord[0]
                        b = coord[1]

                        new_maps[x + a - min_x][y + b - min_y] = idx

                    is_done = True
                    break
            if is_done:
                break

    #print("새 용기 이동 후")
    #for z in range(0, n):
    #    print(new_maps[z])

    # 실험 결과 기록
    visited = []
    neighbor_list = set()
    for x in range(0, n):
        for y in range(0, n):
            if new_maps[x][y] != 0 and [x, y] not in visited:
                check_neighbor(x, y, visited, new_maps[x][y], neighbor_list)

    total = 0

    # print(neighbor_list)

    for frozen_pair in neighbor_list:
        pair = list(frozen_pair)
        a = pair[0]
        b = pair[1]
        a_size = get_size(a, sizes)
        b_size = get_size(b, sizes)

        total += a_size * b_size

    print(total)
    #print()

    maps = copy.deepcopy(new_maps)