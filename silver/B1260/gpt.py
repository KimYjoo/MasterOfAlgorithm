from collections import deque
import sys
def slv():
    N, M, V = map(int, sys.stdin.readline().split())
    table = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        table[u].append(v)
        table[v].append(u)
    
    for i in table:
        i.sort()

    print(' '.join(map(str, DFS(table, V))))
    print(' '.join(map(str, BFS(table, V))))

def BFS(table, V):
    result = []
    visited = [False] * len(table)
    queue = deque([V])
    visited[V] = True
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neigh in table[node]:
            if not visited[neigh] :
                visited[neigh] = True
                queue.append(neigh)

    return result

def DFS(table, V):
    result = []
    visited = [False] * len(table)
    stack = deque([V])
    
    while stack:
        node = stack.pop()
        if not visited[node] :
            result.append(node)
        visited[node] = True
        for neigh in reversed(table[node]):
            if not visited[neigh]:
                stack.append(neigh)
    
    return result

if __name__ == "__main__" :
    slv()