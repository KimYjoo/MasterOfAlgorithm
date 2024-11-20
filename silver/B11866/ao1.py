from collections import deque
max_num, move_range = map(int, input().split())
arr = deque(map(str, list(range(1, max_num + 1))))
now_idx = 0

res = []
while len(arr) != 0:
    for _ in range(move_range-1):
        arr.append(arr.popleft())
    res.append(arr.popleft())
    
print(f"<{str(', '.join(res))}>")