import sys
import itertools

def slv():
    N, M = map(int, sys.stdin.readline().split())

    cards = map(int, sys.stdin.readline().split())

    perms = list(itertools.permutations(cards, 3))

    biggiest_num = 0
    for perm in perms:
        if biggiest_num < sum(perm) <= M:
            biggiest_num = sum(perm)
    
    print(biggiest_num)


if __name__ == "__main__":
    slv()