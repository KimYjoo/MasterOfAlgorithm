import sys
PAIR = {')':'(', ']':'['}

def slv():
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '.':
            break
        print('yes' if main_algo(line) else 'no')


def main_algo(line):
    brackets = []

    for letter in line:
        if letter in '([':
            brackets.append(letter)  
        elif letter in ')]':
            if (not brackets) or brackets[-1] != PAIR[letter]:
                return False
            brackets.pop()
    return not brackets

if __name__ == "__main__":
    slv()