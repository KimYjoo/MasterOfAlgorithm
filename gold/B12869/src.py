from collections import deque

MUTAL_DMG_CASES = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 9, 3], [1, 3, 9]]

def slv():
    N = int(input().strip())
    scv_input = list(map(int, input().split()))
    print(get_attack_count(scv_input, N))

def get_attack_count(scv_input, N):
    scv_lifes = [0] * 3
    for i in range(N):
        scv_lifes[i] = scv_input[i]

    visited = [[[0] * 64 for _ in range(64)] for i in range(64)]
    visited[scv_lifes[0]][scv_lifes[1]][scv_lifes[2]] = 0
    bag = deque([scv_lifes])

    while bag:
        scv1, scv2, scv3 = bag.popleft()

        if visited[0][0][0] > 0 : break

        for dmg1, dmg2, dmg3 in MUTAL_DMG_CASES:
            nscv1 = max(scv1 - dmg1, 0)
            nscv2 = max(scv2 - dmg2, 0)
            nscv3 = max(scv3 - dmg3, 0)
            if visited[nscv1][nscv2][nscv3] == 0:
                visited[nscv1][nscv2][nscv3] = visited[scv1][scv2][scv3] + 1
                bag.append([nscv1, nscv2, nscv3])

    return visited[0][0][0]

if __name__ == "__main__":
    slv()