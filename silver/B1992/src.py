import sys

def slv():
    N = int(sys.stdin.readline().strip())
    graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
    print(main_algo(graph, 0, 0, N))

def main_algo(graph, x, y, edge_size):
    if edge_size > 1:
        half_edge = int(edge_size / 2)
        #왼쪽 위
        left_up = main_algo(graph, x, y, half_edge)
        #오른쪽 위
        right_up = main_algo(graph, x + half_edge, y, half_edge)
        #왼쪽 아래
        left_down = main_algo(graph, x, y + half_edge, half_edge)
        #오른쪽 아래
        right_down = main_algo(graph, x + half_edge, y + half_edge, half_edge)

        quarter = left_up + right_up + left_down + right_down 
        if len(quarter) == 4:
            if left_up == left_down and right_up == right_down and left_up == right_up:
                return left_up
        return f"({quarter})"

    else:
        return graph[y][x]
if __name__ == "__main__":
    slv()