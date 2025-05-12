DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]

def slv():
    R, C = map(int, input().split())
    graph = [list(map(str, input().strip())) for _ in range(R)]
    j_loca = get_location(graph, 'J')
    f_loca = get_location(graph, 'F')
    print(escape_jihoon(graph, R, C, j_loca, f_loca))

    
def escape_jihoon(graph, R, C, j_loca, f_loca):
    hour = 0
    while True:
        hour += 1
        f_loca = fire_ex(graph, f_loca, R, C)
        can_exit, j_loca = jihoon_move(graph, j_loca, R, C)
        if can_exit:
            return hour
        if not j_loca:
            return 'IMPOSSIBLE'

def get_location(graph, stuff):
    locations = []
    for y, row in enumerate(graph):
        for x, value in enumerate(row):
            if value == stuff:
                locations.append((y, x))
    return locations

def fire_ex(graph, f_loca, R, C):
    temp = []
    for y, x in f_loca:
        for dy, dx in zip(DY, DX):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if graph[ny][nx] != '#' and graph[ny][nx] != 'F':
                    graph[ny][nx] = 'F'
                    temp.append((ny, nx))
    return temp

def jihoon_move(graph, j_loca, R, C):
    temp = []
    for y, x in j_loca:
        for dy, dx in zip(DY, DX):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if graph[ny][nx] == '.':
                    graph[ny][nx] = 'J'
                    temp.append((ny, nx))
            else:
                return True, None
    return False, temp
if __name__ == "__main__":
    slv()