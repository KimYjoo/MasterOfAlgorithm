import sys

def slv():
    T = int(sys.stdin.readline())
    for _ in range(T):
        H, W, N = list(map(int, sys.stdin.readline().split()))
        ho, cheong = list(map(str, main_algo(W, H, N)))
        if len(ho) < 2:
            ho = "0" + ho
             
        print(cheong+ho)

def main_algo(W, H, N):
    for w in range(W):
            for h in range(H):
                N = N - 1
                if N == 0:
                    return (w+1, h+1)

if __name__ == "__main__":
    slv()