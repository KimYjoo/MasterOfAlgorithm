import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    a,b = map(int, sys.stdin.readline().split())
    num = (a ** b) % 10
    count = int((a ** b) / 10)

    if num == 0 :
        print(10)
    else:
        print(num)