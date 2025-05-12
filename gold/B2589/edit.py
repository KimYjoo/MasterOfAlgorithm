from collections import deque

DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]

def slv():
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    ret = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 'L' and not visited[y][x]:
                lands = bfs_findLand(graph, visited, n, m, (y, x))
                _, start = bfs_distance(graph, n, m, lands[0])
                max_distance, _ = bfs_distance(graph, n, m, start)
                ret = max(ret, max_distance)
    print(ret)

def bfs_distance(graph, n, m, start):
    max_distance = 0
    max_land = start
    distance = [[-1] * m for _ in range(n)]
    distance[start[0]][start[1]] = 0
    bag = deque([start])
    while bag:
        y, x = bag.popleft()
        for dy, dx in zip(DY, DX):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 'L' and distance[ny][nx] == -1:
                    bag.append((ny,nx))
                    distance[ny][nx] = distance[y][x] + 1
                    if max_distance < distance[ny][nx]:
                        max_distance = distance[ny][nx]
                        max_land = (ny, nx)
    return max_distance, max_land

def bfs_findLand(graph, visited, n, m, start):
    bag = deque([start])
    visited[start[0]][start[1]] = True
    land = []
    land.append(start)
    while bag:
        y, x = bag.popleft()
        for dy, dx in zip(DY, DX):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 'L' and not visited[ny][nx]:
                    bag.append((ny,nx))
                    visited[ny][nx] = True
                    land.append((ny,nx))
    return land

if __name__ == "__main__":
    slv()