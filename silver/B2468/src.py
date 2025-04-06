# 필요한 그래프는 3개
# 입력(높이) 그래프
# 잠긴 지역 그래프
# 방문 그래프

import sys
from collections import deque
DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

def slv():
    N = int(sys.stdin.readline().strip())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    max_height = max(map(max, graph))

    result = 0
    for rain_height in range(0, max_height + 1):
        visited = [[False]*N for _ in range(N)]
        bag = deque()
        rand = 0

        for start_y in range(N):
            for start_x in range(N):
                if graph[start_y][start_x] <= rain_height or visited[start_y][start_x]: continue
                bag = deque([(start_x, start_y)])
                visited[start_y][start_x] = True
                while bag:
                    x, y = bag.pop()
                    for dx, dy in zip(DX, DY):
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < N: 
                            if graph[ny][nx] > rain_height and not visited[ny][nx]:
                                visited[ny][nx] = True
                                bag.append((nx, ny))
                rand += 1
        result = max(rand, result)

    print(result)


if __name__ == "__main__":
    slv()