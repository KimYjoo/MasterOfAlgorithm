# 최소한의 칸의 수 -> 너비우선탐색 BFS

import sys
from collections import deque

def slv():
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    distance_graph = [[-1] * M for _ in range(N)]
    distance_graph[0][0] = 0
    start_node = [0, 0, 1]
    main_algo(graph, distance_graph, start_node, N, M)

def main_algo(graph, distance_graph, start_node, max_y, max_x):
    DX = [1, -1, 0, 0]
    DY = [0, 0, 1, -1]
    bag = deque([(start_node[0], start_node[1], start_node[2])])
    while bag :
        now_node = bag.popleft()
        now_x = now_node[0]
        now_y = now_node[1]
        now_distance = now_node[2]
        distance_graph[now_y][now_x] = now_distance

        for idx in range(4):
            candidate_x = now_x + DX[idx]
            candidate_y = now_y + DY[idx]
            if candidate_x < 0 or candidate_x >= max_x or candidate_y < 0 or candidate_y >= max_y :
                continue
            if graph[candidate_y][candidate_x] == 0 or distance_graph[candidate_y][candidate_x] >= 0:
                continue
            bag.append([candidate_x, candidate_y, now_distance + 1])
    print(distance_graph[max_y-1][max_x-1])




if __name__ == "__main__":
    slv()