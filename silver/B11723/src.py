import sys
def add(param):
    S = param[0]
    x = param[1][1]
    if not x in S :
        S.add(x)
def remove(param):
    S = param[0]
    x = param[1][1]
    if x in S:
        S.remove(x)
def check(param):
    S = param[0]
    x = param[1][1]
    print(int(x in S))
def toggle(param):
    S = param[0]
    x = param[1][1]
    if x in S:
        S.remove(x)
    else:
        S.add(x)
def all(param):
    S = param[0]
    S.update(map(str, list(range(1,21))))
def empty(param):
    S = param[0]
    S.clear()

def slv():
    S = set([])
    set_commands = {
        'add': lambda x: S.add(x),
        'remove': lambda x: S.discard(x),  # remove 대신 discard 사용으로 오류 방지
        'check': lambda x: print(1 if x in S else 0),
        'toggle': lambda x: S.remove(x) if x in S else S.add(x),
        'all': lambda _: S.update(range(1, 21)),
        'empty': lambda _: S.clear()
    }
    cases = int(sys.stdin.readline())
    for _ in range(cases):
        input = sys.stdin.readline().split()
        x = None
        if len(input) > 1 :
            x = int(input[1])
        command = input[0]

        set_commands[command](x)
if __name__ == "__main__":
    slv()