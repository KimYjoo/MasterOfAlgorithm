max_num, move_range = map(int, input().split())
arr = list(map(str, list(range(1, max_num + 1))))
now_idx = 0

res = []
while len(arr) >= 1:
    now_idx = (now_idx + move_range - 1)%len(arr)
    res.append(arr.pop(now_idx))

print(f"<{str(', '.join(res))}>")