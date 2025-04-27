import sys

def slv():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        
        x = sys.stdin.readline().strip()
        if main_algo(x):
            print('YES')
        else:
            print('NO')

def main_algo(x):
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
    
if __name__ == "__main__":
    slv()