import sys
from collections import deque

def slv():
    n = int(sys.stdin.readline().strip())
    graph = [[False] * (n + 1) for _ in range(n+1)]
    visited = [False] * (n + 1)
    computers = int(sys.stdin.readline().strip())

    for _ in range(computers):
        x, y = map(int, sys.stdin.readline().split())
        
        graph[x][y] = True
        graph[y][x] = True
    print(main_algo(graph, visited, 1))

def main_algo(graph, visited, node):
    bag = deque([node])
    visited[node] = True
    count = 0
    while bag:
        now_node = bag.popleft()
        for index in range(1, len(graph[now_node])):
            if graph[now_node][index] and not visited[index]:
                visited[index] = True
                bag.append(index)
                count += 1
    return count 


if __name__ == "__main__":
    slv()

