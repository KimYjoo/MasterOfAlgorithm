import sys
from collections import deque

# def slv():
#     T = int(sys.stdin.readline().strip())
#     queue = deque()
#     output = []
#     for _ in range(T):
#         command = sys.stdin.readline().split()
#         command_name = command[0]
        

#         if command_name == "push":
#             queue.append(int(command[1]))
#         elif command_name == "pop":
#             if queue:
#                 output.append(queue.popleft())
#             else:
#                 output.append(-1)
#         elif command_name == "size":
#             output.append(len(queue))
#         elif command_name == "empty":
#             if queue:
#                 output.append(0)
#             else:
#                 output.append(1)
#         elif command_name == "front":
#             if queue:
#                 output.append(queue[0])
#             else:
#                 output.append(-1)
#         elif command_name == "back":
#             if queue:
#                 output.append(queue[-1])
#             else:
#                 output.append(-1)
#     print('\n'.join(map(str,output)))

def slv():
    T = int(sys.stdin.readline().strip())
    queue = deque()
    output = []

    def push(x): queue.append(x)
    def pop(): output.append(queue.popleft() if queue else -1)
    def size(): output.append(len(queue))
    def empty(): output.append(0 if queue else 1)
    def front(): output.append(queue[0] if queue else -1)
    def back(): output.append(queue[-1] if queue else -1)

    commands = {
        'pop' : pop,
        'size' : size,
        'empty' : empty,
        'front' : front,
        'back' : back,
    }

    for _ in range(T):
        cmd = command = sys.stdin.readline().split()
        if cmd[0] == 'push':
            push(int(cmd[1]))
        else:
            commands[cmd[0]]()
    
    print('\n'.join(map(str, output)))
    
if __name__ == "__main__":
    slv()