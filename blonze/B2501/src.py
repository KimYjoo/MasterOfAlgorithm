import sys

N, K = map(int, sys.stdin.readline().split())

arr = []
for i in range(1, N + 1):
    if N % i == 0:
        arr.append(i)
if len(arr) >= K:
    print(arr[K-1])
else:
    print(0)