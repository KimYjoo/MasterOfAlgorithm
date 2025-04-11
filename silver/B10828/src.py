import sys
from collections import deque

def slv():
    T = int(sys.stdin.readline().strip())
    stack = deque()
    output = []

    def push(x): stack.append(x)
    def pop(): output.append(stack.pop() if stack else -1)
    def size(): output.append(len(stack))
    def empty(): output.append(0 if stack else 1)
    def top(): output.append(stack[-1] if stack else -1)

    commands = {
        'pop' : pop,
        'size' : size,
        'empty' : empty,
        'top' : top,
    }

    for _ in range(T):
        cmd = sys.stdin.readline().split()
        if cmd[0] == 'push':
            push(int(cmd[1]))
        else:
            commands[cmd[0]]()
    
    print('\n'.join(map(str, output)))
    
if __name__ == "__main__":
    slv()