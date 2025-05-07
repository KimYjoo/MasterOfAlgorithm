import sys
from collections import deque

input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
edges = [[] for _ in range(N+1)]
idx = 2
for _ in range(M):
    a = int(data[idx])
    b = int(data[idx+1])
    edges[b].append(a)
    idx += 2

visited = [False] * (N + 1)

def bfs(start):
    count = 1
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for nxt in edges[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1
    return count

max_count = 0
result = []

for i in range(1, N + 1):
    for j in range(1, N + 1):
        visited[j] = False
    cnt = bfs(i)
    if cnt > max_count:
        max_count = cnt
        result = [i]
    elif cnt == max_count:
        result.append(i)

print(*result)
