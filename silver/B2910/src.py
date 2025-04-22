import sys

def slv():
    N, C = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    bag = {}
    for i in arr:
        if i in bag:
            bag[i] += 1
        else:
            bag[i] = 1
    for a in sorted(bag.items(), key = lambda x: x[1], reverse=True):
        for _ in range(a[1]):
            print(a[0], end=' ')
    print()

if __name__ == "__main__":
    slv()