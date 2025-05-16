from collections import deque
def slv():
    start, end = map(int, input().split())
    remember = [-1] * 200004
    print( bfs_shortest_path(start, end, remember) - 1 )

    node = end
    result = [node]
    while node != start:
        node = remember[node]
        result.append(node)
    
    result.reverse()
    print(*result)

def bfs_shortest_path(start, end, remember):
    bag = deque([start])
    visited = [0] * 200004
    visited[start] = 1
    while bag:
        curr = bag.popleft()
        if curr == end:
            return visited[end]
        for node in (curr + 1, curr - 1, curr * 2):
            if 0 <= node <= 100000:
                if not visited[node]:
                    bag.append(node)
                    visited[node] = visited[curr] + 1
                    remember[node] = curr

if __name__ == "__main__":
    slv()