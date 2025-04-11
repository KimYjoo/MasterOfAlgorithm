import sys
from collections import deque

def slv():
    n = int(sys.stdin.readline().strip())
    graph = [[False] * n for _ in range(n+1)]
    visited = [False] * (n + 1)
    computers = int(sys.stdin.readline().strip())

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        
        graph[x][y] = True
        graph[y][x] = True
    
def main_algo(graph, visited, node):
    bag = deque([node])
    visited[node] = True
    while bag:
        bag.pop
        for index in graph[node]:


    

