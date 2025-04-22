import sys

arr = map(int, sys.stdin.readline().split())

answer = [1, 1, 2, 2, 2, 8]

for a, b in zip(arr, answer):
    print(b-a,  end=' ')