import sys
from collections import deque
DY = [-1, 0, 1, 0]
DX = [0, 1, 0, -1]

def slv():
    N, M = map(int, sys.stdin.readline().split()) # 세로, 가로
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    time = 0
    cheese = 0
    while True:
        c_spot = main_algo(graph,N,M)
        if not c_spot:
            break
        cheese = len(c_spot)
        time += 1
        for y, x in c_spot:
            graph[y][x] = 0
    print(f'{time}\n{cheese}')



def main_algo(graph,N,M):
    visited = [[False] * M for _ in range(N)]
    bag = deque([(0,0)])
    c_spot = []
    visited[0][0] = True
    while bag:
        ny, nx = bag.pop()
        for dy, dx in zip(DY, DX):
            newY = ny + dy
            newX = nx + dx
            if 0 <= newX < M and 0 <= newY < N:
                if graph[newY][newX] == 0 and not visited[newY][newX]:
                    bag.append((newY, newX))
                    visited[newY][newX] = True
                if graph[newY][newX] == 1:
                    graph[newY][newX] = 2
                    c_spot.append((newY, newX))

    return c_spot

if __name__ == "__main__":
    slv()

