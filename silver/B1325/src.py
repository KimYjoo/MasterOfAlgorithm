import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
for _ in range(M):
    trusting, trusted = map(int, sys.stdin.readline().split())
    edges[trusted].append(trusting)

def bfs(node):
    visited[node] = True
    bag = deque([node])
    count = 1
    while bag:
        next_node = bag.popleft()
        for i in edges[next_node]:
            if not visited[i]:
                visited[i] = True
                bag.append(i)
                count += 1
    return count

max_count = -1
result = []

for i in range(1, N + 1):
    cnt = bfs(i)
    for j in range(1, N + 1):
        visited[j] = False
    if cnt > max_count:
        max_count = cnt
        result = [i]
    elif cnt == max_count:
        result.append(i)

print(*result)