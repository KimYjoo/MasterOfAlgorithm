from collections import deque

DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]

def slv():
    n, m = map(int, input().split())
    graph = [list(input().strip()) for _ in range(n)]
    ret = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 'L':
                ret = max(bfs(graph, n, m, (y, x)), ret)

    print(ret)

def bfs(graph, n, m, start):
    distance = [[-1] * m for _ in range(n)]
    bag = deque([start])
    distance[start[0]][start[1]] = 0
    max_distance = 0
    while bag:
        y, x = bag.popleft()
        for dy, dx in zip(DY, DX):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 'L' and distance[ny][nx] == -1:
                    bag.append((ny,nx))
                    distance[ny][nx] = distance[y][x] + 1
                    max_distance = max(max_distance, distance[ny][nx])
    return max_distance


if __name__ == "__main__":
    slv()