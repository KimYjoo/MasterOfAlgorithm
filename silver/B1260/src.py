from collections import deque
import sys
def slv():
    N, M, V = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(M):
        arr.append(list(map(int, sys.stdin.readline().split())))
    arr_rev = [[i[1], i[0]]for i in arr]
    arr += arr_rev
    arr.sort(key = lambda k : (k[0], k[1]))
    table = [[] for _ in range(N + 1)]
    for i in arr :
        table[i[0]].append(i[1])

    print(' '.join(DFS(table, V)))
    print(' '.join(BFS(table, V)))

def BFS(table, V):
    result = [str(V)]
    visited = [False for _ in range(len(table))]
    visited[V] = True
    queue = deque(table[V])
    while(len(queue) != 0):
        candi = queue.popleft()
        if not visited[candi] :
            result.append(str(candi))
            visited[candi] = True
            [queue.append(i) for i in table[candi]]
    return result

def DFS(table, V):
    result = [str(V)]
    visited = [False for _ in range(len(table))]
    visited[V] = True
    stack = deque([i for i in table[V][::-1]])
    while(len(stack) != 0):
        candi = stack.pop()
        if not visited[candi]:
            result.append(str(candi))
            visited[candi] = True
            [stack.append(i) for i in table[candi][::-1]]
    return result

if __name__ == "__main__" :
    slv()