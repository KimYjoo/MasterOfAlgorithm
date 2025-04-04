import sys

def slv():
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())

    print(a+b-c)
    print(int(str(a)+str(b)) - c)

if __name__ == "__main__":
    slv()