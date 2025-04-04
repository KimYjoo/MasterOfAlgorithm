# 최소한의 칸의 수 -> 너비우선탐색 BFS

import sys
from collections import deque

def slv():
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    # distance_graph = [[-1] * M] * N
    distance_graph = [[0] * M for _ in range(N)]
    start_node = (0, 0)
    bag = deque()
    bag.append(start_node)

    main_algo(graph, distance_graph, N, M, bag)

def main_algo(graph, distance_graph, max_y, max_x, bag):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while bag :
        x, y = bag.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < max_x and 0 <= ny < max_y :
                if graph[ny][nx] == 1 and distance_graph[ny][nx] == 0:
                    bag.append((nx, ny))
                    distance_graph[ny][nx] = distance_graph[y][x] + 1

    print(distance_graph[max_y-1][max_x-1] + 1)




if __name__ == "__main__":
    slv()