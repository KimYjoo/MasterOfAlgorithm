import sys

def slv():
    n = int(sys.stdin.readline().strip())
    sequence = list(map(int, sys.stdin.readline().split()))
    stack = []
    result = [-1] * n

    for i in range(n):
        while stack and sequence[stack[-1]] < sequence[i]:
            result[stack[-1]] = sequence[i]
            stack.pop()
        stack.append(i)

    print(*result)

if __name__ == "__main__":
    slv()