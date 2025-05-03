import sys

N = int(sys.stdin.readline().strip())
arr = []
for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    arr.append({'weight':weight, 'height':height, 'index':i+1, 'rank':0})

arr.sort(key = lambda x : x['height'], reverse=True)
rank = 1
last_weight = 201
for i in range(len(arr)):
    if arr[i]['weight'] < last_weight:
        rank = i + 1
        last_weight = arr[i]['weight']
    arr[i]['rank'] = rank
arr.sort(key= lambda x:x['index'])
ranks = [n['rank'] for n in arr if 'rank' in n]
print(' '.join(map(str, ranks)))


