import sys

T = int(sys.stdin.readline().strip())

bag = set()
for _ in range(T):
    bag.add(int(sys.stdin.readline().strip()))

arr = list(bag)
arr.sort()
print('\n'.join(map(str, arr)))