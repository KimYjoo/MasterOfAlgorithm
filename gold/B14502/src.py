# 지도에서 0인 자리에 1을 끼워본다
# 3개를 넣었을 경우를 조합한다.
# 1. 0의 좌표를 모두 찾는다
# 2. 0의 좌표 중 3개를 고른 조합에 1을 넣어서 안전 지대를 구한다.
# 3. 2번을 반복하여 최대 안전 지대 개수를 구한다. 
import sys
import copy
from collections import deque
from itertools import combinations

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

def slv():
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    empty_rooms = search_room(graph, N, M, 0)
    empty_room_combi = list(combinations(range(len(empty_rooms)), 3))
    max_safe_room = 0
    for new_walls in empty_room_combi:
        new_graph = copy.deepcopy(graph)
        for idx in new_walls:
            wall_x, wall_y = empty_rooms[idx]
            new_graph[wall_y][wall_x] = 1
        virus_spread(new_graph, N, M)
        
        safe_rooms = search_room(new_graph, N, M, 0)
        if len(safe_rooms) > max_safe_room:
            max_safe_room = len(safe_rooms)
    print(max_safe_room)
    
def search_room(graph, N, M, room_num):
    visited = [[False] * M for _ in range(N)]
    coordinates = []
    for y in range(N):
        for x in range(M):
            if graph[y][x] == room_num and not visited[y][x]:
                bag = deque([(x,y)])
                visited[y][x] = True
                coordinates.append((x,y))
                while bag:
                    nx, ny = bag.pop()
                    for dx, dy in zip(DX, DY):
                        candi_x = nx + dx
                        candi_y = ny + dy
                        if 0 <= candi_x < M and 0 <= candi_y < N:
                            if graph[candi_y][candi_x] == room_num and not visited[candi_y][candi_x]:
                                bag.append((candi_x, candi_y))
                                visited[candi_y][candi_x] = True
                                coordinates.append((candi_x, candi_y))
    return coordinates

def virus_spread(graph, N, M):
    visited = [[False] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 2 and not visited[y][x]:
                bag = deque([(x,y)])
                visited[y][x] = True
                while bag:
                    nx, ny = bag.pop()
                    for dx, dy in zip(DX, DY):
                        candi_x = nx + dx
                        candi_y = ny + dy
                        if 0 <= candi_x < M and 0 <= candi_y < N:
                            if graph[candi_y][candi_x] == 0 and not visited[candi_y][candi_x]:
                                bag.append((candi_x, candi_y))
                                visited[candi_y][candi_x] = True
                                graph[candi_y][candi_x] = 2
    
if __name__ == "__main__":
    slv()