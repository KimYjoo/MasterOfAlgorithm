import sys

def slv():
    arr = [int(sys.stdin.readline()) % 42 for _ in range(10)]
    tmp = {}
    for x in arr:
        if not x in tmp:
            tmp[x] = 1
    print(len(tmp))

if __name__ == "__main__":
    slv()