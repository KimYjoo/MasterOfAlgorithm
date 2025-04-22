import sys

def slv():
    H, W = map(int, sys.stdin.readline().split())
    graph = [sys.stdin.readline() for _ in range(H)]
    result = [[0] * W for _ in range(H)]

    for y in range(H):
        cloud_reach = -1
        has_cloud = False
        for x in range(W):
            if has_cloud:
                cloud_reach += 1
            if graph[y][x] == 'c':
                cloud_reach = 0
                has_cloud = True
            result[y][x] = cloud_reach
    for graph in result:
        print(' '.join(map(str, graph)))
            
if __name__ == "__main__":
    slv()