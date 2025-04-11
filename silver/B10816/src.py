import sys

def slv():
    N = int(sys.stdin.readline().strip())
    sangs_cards = map(int, sys.stdin.readline().split())
    M = int(sys.stdin.readline().strip())
    check_cards = map(int, sys.stdin.readline().split())

    sangs_cards_map = {}
    for card in sangs_cards:
        if card in sangs_cards_map:
            sangs_cards_map[card] += 1
        else:
            sangs_cards_map[card] = 1
    
    output = []
    for card in check_cards:
        if card in sangs_cards_map:
            output.append(sangs_cards_map[card])
        else:
            output.append(0)
    print(' '.join(map(str, output)))

if __name__ == "__main__":
    slv()