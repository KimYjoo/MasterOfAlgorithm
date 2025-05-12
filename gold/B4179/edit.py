from collections import deque
import sys
INF = 1000004
DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]

def slv():
    R, C = map(int, sys.stdin.readline().split())
    graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

    jihoon_location = ()
    fire_locations = []
    fire_ex_time = [[INF] * C for _ in range(R)]
    
    for y, row in enumerate(graph):
        for x, value in enumerate(row):
            if value == 'J':
                jihoon_location = (y, x)
            elif value == 'F':
                fire_locations.append((y, x))
                fire_ex_time[y][x] = 1

    fire_bfs(graph, fire_locations, fire_ex_time, R, C)

    time = escape(graph, jihoon_location, fire_ex_time, R, C)
    if time:
        print(time)
    else:
        print('IMPOSSIBLE')


def fire_bfs(graph, fire_locations, distance, R, C):
    bag = deque(fire_locations)
    while bag:
        y, x = bag.popleft()
        for dy, dx in zip(DY, DX):
            ny = dy + y
            nx = dx + x
            if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] != '#' and distance[ny][nx] == INF:
                bag.append((ny, nx))
                distance[ny][nx] = distance[y][x] + 1

def escape(graph, start, fire_graph, R, C):
    distance = [[0] * C for _ in range(R)]
    distance[start[0]][start[1]] = 1
    bag = deque([start])
    while bag:
        y, x = bag.popleft()
        for dy, dx in zip(DY, DX):
            ny = dy + y
            nx = dx + x
            if 0 > ny or ny >= R or 0 > nx or nx >= C :
                return distance[y][x]
            if graph[ny][nx] != '#' and not distance[ny][nx]:
                if distance[y][x] + 1 < fire_graph[ny][nx]:
                    distance[ny][nx] = distance[y][x] + 1
                    bag.append((ny,nx))
    return 0
if __name__ == "__main__":
    slv()