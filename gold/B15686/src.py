# y = r
# x = c
# 치킨 거리 = 집과 가장 가까운 치킨집 사이 거리
# 각 집은 고유의 치킨 거리를 가지고 있다.
# 도시의 치킨 거리 = 모든 치킨 거리의 합
# 도시의 치킨 거리가 가장 작게 될 수 있는 M개의 치킨집을 선택
# 1 <= 집 <= 2N
# M <= 치킨 <= 13


import sys
from itertools import combinations

def slv():
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    house_co = []
    chicken_co = []
    chicken_street = []
    for y in range(N):
        for x in range(N):
            if graph[y][x] == 2:
                chicken_co.append((y, x))
            elif graph[y][x] == 1:
                house_co.append((y, x))
    for chicken in chicken_co:
        temp_street = []
        for house in house_co:
            chicken_y, chicken_x = chicken
            house_y, house_x = house
            temp_street.append(abs(chicken_y - house_y) + abs(chicken_x - house_x))
        chicken_street.append(temp_street)
    
    combi = list(combinations(chicken_street, M))
    min_street = 10000004
    for streets in combi:
        ret = sum([min([streets[y][x] for y in range(M)]) for x in range(len(streets[0]))])
        min_street = min(min_street, ret)

    print(min_street)
if __name__ == "__main__":
    slv()