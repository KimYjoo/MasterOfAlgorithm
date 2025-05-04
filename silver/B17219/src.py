import sys

N, M = map(int, sys.stdin.readline().split())
site_map = {}
for _ in range(N):
    address, password = sys.stdin.readline().split()
    site_map[address] = password


for _ in range(M):
    address = sys.stdin.readline().strip()
    print(site_map[address])