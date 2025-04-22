import sys
from collections import deque

DX = [1, -1, 0, 0, 1, -1, 1, -1]
DY = [0, 0, 1, -1, 1, -1, -1, 1]

def slv():
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0 : break
        graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        count = 0
        for y in range(h):
            for x in range(w):
                if graph[y][x] == 1 and not visited[y][x]:
                    main_algo(graph, visited, x, y, w ,h)
                    count += 1
        print(count)


def main_algo(graph, visited, x, y, w, h):
    bag = deque([(x,y)])
    visited[y][x] = True
    while bag:
        nx, ny = bag.popleft()
        for dx, dy in zip(DX, DY):
            now_x = dx + nx
            now_y = dy + ny
            if 0 <= now_x < w and 0 <= now_y < h:
                if graph[now_y][now_x] == 1 and not visited[now_y][now_x]:
                    bag.append((now_x, now_y))
                    visited[now_y][now_x] =True

if __name__ == "__main__":
    slv()

        

        

