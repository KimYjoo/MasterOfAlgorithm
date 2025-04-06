import sys
from collections import deque
DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

def slv():
    T = int(sys.stdin.readline())

    for _ in range(T):
        graph_width, graph_height, K = list(map(int, sys.stdin.readline().split()))
        graph = [[0] * graph_width for _ in range(graph_height)]
        visited = [[False] * graph_width for _ in range(graph_height)]
        for _ in range(K):
            x, y = list(map(int, sys.stdin.readline().split()))
            graph[y][x] = 1
        main_algo(graph, visited)

def main_algo(graph, visited):
    baechoo = 0
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if graph[y][x] == 1 and not visited[y][x]:
                baechoo = baechoo + 1
                dfs(graph, visited, x, y)
    print(baechoo)
    
def dfs(graph, visited, x, y):
    stack = deque()
    stack.append((x, y))
    visited[curr_y][curr_x] = True
    while(stack):
        curr_x, curr_y = stack.pop()
        for i in range(4):
            nx = curr_x + DX[i]
            ny = curr_y + DY[i]
            if( 0 <= nx < len(graph[0]) and 0 <= ny < len(graph)) :
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    stack.append((nx, ny))
                    visited[curr_y][curr_x] = True


if __name__ == "__main__":
    slv()