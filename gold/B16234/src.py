from collections import deque
DY = [-1, 0, 1, 0]
DX = [0, 1, 0, -1]

def slv():
    N, L, R = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)] 
    is_moved = True
    count = -1
    while is_moved:
        count += 1
        is_moved = False
        union = [[False] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if not union[y][x]:
                    if bfs(graph, union, N, L, R, (y, x)):
                        is_moved = True
    print(count)

def bfs(graph, union, N, L, R, start):
    union_list = [start]
    bag = deque([start])
    union[start[0]][start[1]] = True
    people_sum = graph[start[0]][start[1]]
    is_moved = False
    while bag:
        y, x = bag.popleft()
        for dy, dx in zip(DY, DX):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and not union[ny][nx] and L <= abs(graph[ny][nx] - graph[y][x]) <= R:
                bag.append((ny,nx))
                union[ny][nx] = True
                union_list.append((ny, nx))
                people_sum += graph[ny][nx]
                is_moved = True
    if is_moved:
        people_move(graph, union_list)
    return is_moved

def people_move(graph, union_list):
    people = sum([graph[cy][cx] for cy, cx in union_list])
    union_num = len(union_list)
    for cy, cx in union_list:
        graph[cy][cx] = int(people / union_num)


if __name__ == "__main__":
    slv()