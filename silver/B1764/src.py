import sys

N, M = map(int, sys.stdin.readline().split())

map = dict()
for _ in range(N) :
    map[sys.stdin.readline()] = None

result = []
for _ in range(M) :
    tmp = sys.stdin.readline() 
    if tmp in map :
        result.append(tmp)

print(len(result))
result.sort()
print(''.join(result))
