from collections import deque

def slv():
    start, end = map(int, input().split())

    if start == end:
        print(0)
        return
    
    is_found, time = bfs(start, end)
    print(time if is_found else -1)

def bfs(start, end):
    visited = [[0] * 500004 for _ in range(2)]
    visited[0][start] = 1
    bag = deque([start])
    young = end
    time = 1
    
    while bag:
        young += time
        if young > 500000:
            return False, None
        
        if visited[time % 2][young]:
            return True, time
        
        bag_len = len(bag)
        for _ in range(bag_len):
            curr = bag.popleft()
            for moved in (curr + 1, curr - 1, curr * 2):
                if 0 <= moved <= 500000 and not visited[time % 2][moved]:
                    if moved == young:
                        return True, time
                    visited[time % 2][moved] = visited[(time + 1) % 2][curr] + 1
                    bag.append(moved)
        time += 1
    return False, None

if __name__ == "__main__":
    slv()