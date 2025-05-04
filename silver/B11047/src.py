import sys

N, K = map(int, sys.stdin.readline().split())
states = []
for _ in range(N):
    states.append(int(sys.stdin.readline().strip()))
states.sort(reverse=True)
temp = K
count = 0
for state in states:
    count += temp // state
    temp %= state
    if temp == 0:
        break
print(count)