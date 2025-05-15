from collections import deque

INF = 987654321
def slv():
    start, end = map(int, input().split())
    visited = [INF] * 100000
    count = find_dong(start, end, visited)

    print(visited[end])
    print(count)

def find_dong(start, end, visited):
    bag = deque([(start, 0)])
    min_time = INF
    count = 0
    while bag:
        now_loca, time = bag.popleft()
        if now_loca == end :
            if not min_time :
                min_time = time
            count += 1

        go_back = now_loca - 1
        go_front = now_loca + 1
        teleport = now_loca * 2
        
        if min_time >= time + 1:
            append_node(go_front, visited, bag, time + 1)
            append_node(go_back, visited, bag, time + 1)
            append_node(teleport, visited, bag, time + 1)
    
    return count


def append_node(node, visited, bag, time):
    if 0 <= node < 100000 and time <= visited[node]:
        visited[node] = time
        bag.append((node, time))

if __name__ == "__main__":
    slv()