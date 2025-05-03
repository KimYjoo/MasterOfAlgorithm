import sys

N = int(sys.stdin.readline().strip())
arr = []
for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    arr.append({'weight':weight, 'height':height, 'rank':0})

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if arr[j]['weight'] > arr[i]['weight'] and arr[j]['height'] > arr[i]['height'] :
            rank += 1
    arr[i]['rank'] = rank

ranks = [n['rank'] for n in arr if 'rank' in n]
print(' '.join(map(str, ranks)))