# 지도에서 0인 자리에 1을 끼워본다
# 3개를 넣었을 경우를 조합한다.
# 1. 0의 좌표를 모두 찾는다
# 2. 0의 좌표 중 3개를 고른 조합에 1을 넣어서 안전 지대를 구한다.
# 3. 2번을 반복하여 최대 안전 지대 개수를 구한다. 
import sys
from collections import deque
from itertools import combinations

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

def slv():
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    empty_rooms = [(x,y) for y in range(N) for x in range(M) if graph[y][x] == 0]
    max_safe = 0
    virus_point = [(x,y) for y in range(N) for x in range(M) if graph[y][x] == 2]

    for walls in combinations(empty_rooms, 3):
        new_graph = [row[:] for row in graph]
        for x, y in walls:
            new_graph[y][x] = 1
        virus_spread(new_graph, virus_point, N, M)
        safe = sum(row.count(0) for row in new_graph)
        max_safe = max(max_safe, safe)
        
    print(max_safe)


def virus_spread(graph, virus_point, N, M):
    bag = deque(virus_point)
    while bag:
        nx, ny = bag.pop()
        for dx, dy in zip(DX, DY):
            candi_x = nx + dx
            candi_y = ny + dy
            if 0 <= candi_x < M and 0 <= candi_y < N:
                if graph[candi_y][candi_x] == 0:
                    bag.append((candi_x, candi_y))
                    graph[candi_y][candi_x] = 2
    
if __name__ == "__main__":
    slv()