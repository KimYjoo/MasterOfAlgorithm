import sys

def slv():
    while True:
        line = sys.stdin.readline().rstrip()
        
        if line == '.':
            break
        if main_algo(line):
            print('yes')
        else:
            print('no')

def main_algo(line):
    brackets = []
    for letter in line:
        if letter == '(' or letter == '[':
            brackets.append(letter)  
        elif letter == ')':
            if (not brackets) or brackets[-1] != '(':
                return False
            brackets.pop()
        elif letter == ']':
            if (not brackets) or brackets[-1] != '[':
                return False
            brackets.pop()
        elif letter == '.':
            break
    return not brackets

if __name__ == "__main__":
    slv()