from collections import deque

INF = float('inf')

def slv():
    start, end = map(int, input().split())
    visited = [INF] * 500004
    end_moved = [end] * 500004
    result = bfs_fastest_reach(start, end, visited, end_moved)
    print(result)

def bfs_fastest_reach(start, end, visited, end_moved):
    bag = deque([start])
    visited[start] = 1
    end_moved[start] = end

    while bag:
        curr = bag.popleft()
        print(f'time = {visited[curr] - 1} : ', end = '')
        print(f'curr = {curr}')
        if end_moved[curr] == curr:
            return visited[curr] - 1
        if end_moved[curr] > curr:
            bag.append(curr - 1)
            visited[curr - 1] = visited[curr] + 1
            end_moved[curr - 1] = end_moved[curr] + visited[curr]
            continue
        for moved in (curr + 1, curr - 1, curr * 2):
            if 0 > moved or moved > 500000:
                continue
            if visited[moved] >= visited[curr] + 1:
                bag.append(moved)
                visited[moved] = visited[curr] + 1
                end_moved[moved] = end_moved[curr] + visited[curr]
            
if __name__ == "__main__":
    slv()