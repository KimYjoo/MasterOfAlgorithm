# from collections import deque

# INF = 987654321
# def slv():
#     start, end = map(int, input().split())
#     visited = [INF] * 100001
#     count = find_dong(start, end, visited)

#     print(visited[end])
#     print(count)

# def find_dong(start, end, visited):
#     bag = deque([(start, 0)])
#     visited[start] = 0
#     min_time = INF
#     count = 0
#     while bag:
#         now_loca, time = bag.popleft()
#         if now_loca == end :
#             if min_time > time:
#                 min_time = time
#                 count = 1
#             elif min_time == time:
#                 count += 1
#             continue

#         go_back = now_loca - 1
#         go_front = now_loca + 1
#         teleport = now_loca * 2
        
#         if min_time >= time + 1:
#             append_node(go_front, visited, bag, time + 1)
#             append_node(go_back, visited, bag, time + 1)
#             append_node(teleport, visited, bag, time + 1)
    
#     return count


# def append_node(node, visited, bag, time):
#     if 0 <= node <= 100000 and time <= visited[node]:
#         visited[node] = time
#         bag.append((node, time))

# if __name__ == "__main__":
#     slv()



from collections import deque

def slv():
    start, end = map(int, input().split())
    if start == end:
        print("0\n1")
    else:
        visited = [0] * 200004
        count = find_dong(start, end, visited)
        print(visited[end] - 1)
        print(count[end])

def find_dong(start, end, visited):
    count = [0] * 100004
    bag = deque([start])
    visited[start] = 1
    count[start] = 1
    while bag:
        now_loca = bag.popleft()
        for node in (now_loca - 1, now_loca + 1, now_loca * 2):
            if 0 <= node <= 100000:
                if not visited[node]:
                    bag.append(node)
                    visited[node] = visited[now_loca] + 1
                    count[node] += count[now_loca]
                elif visited[node] == visited[now_loca] + 1:
                    count[node] += count[now_loca]
    return count

if __name__ == "__main__":
    slv()