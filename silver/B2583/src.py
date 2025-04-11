# M = 세로, N = 가로, K = 직사각형 개수
# K개의 직사각형 좌표 왼쪽 아래 xy좌표, 오른쪽 위 xy좌표
import sys
from collections import deque

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]
def slv():
    M, N, K = list(map(int, sys.stdin.readline().split()))    
    graph = [[True]*N for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    for _ in range(K):
        left_down_x, left_down_y, right_up_x, right_up_y = list(map(int, sys.stdin.readline().split())) 

        width = right_up_x - left_down_x 
        height = right_up_y - left_down_y 

        for y in range(left_down_y, left_down_y + height):
            for x in range(left_down_x, left_down_x + width):
                graph[y][x] = False
        
    area_count = 0
    area_size_list = []
    for y in range(M):
        for x in range(N):
            if graph[y][x] and not visited[y][x]:
                bag = deque([(x,y)])
                visited[y][x] = True
                area_size = 0
                while bag :
                    now_x, now_y = bag.popleft()
                    for dx, dy in zip(DX, DY):
                        nx = now_x + dx
                        ny = now_y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if graph[ny][nx] and not visited[ny][nx]:
                                bag.append((nx, ny))
                                visited[ny][nx] = True
                    area_size += 1
                area_size_list.append(area_size)
                area_count += 1

    print(area_count)
    area_size_list.sort()
    # [print(idx, end=" ") for idx in area_size_list]
    print(' '.join(map(str, area_size_list)))

if __name__ == "__main__":
    slv()