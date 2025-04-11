import sys

def slv():
    while True:
        a, b, c = list(map(int, sys.stdin.readline().split()))
        if a + b + c == 0:
            break
        long_line = max(a, b, c)
        last_lines = a ** 2 + b ** 2 + c ** 2 - long_line ** 2
        if long_line ** 2 == last_lines :
            print("right")
        else:
            print("wrong")

if __name__ == "__main__":
    slv()