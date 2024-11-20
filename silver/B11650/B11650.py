cases = int(input())
arr = [list(map(int,input().split())) for i in range(cases)]

arr.sort(key=lambda x : x[1])

result = {}
for i in arr:
    if i[0] in result:
        result[i[0]].append(i[1])
    else:
        result[i[0]] = [i[1]]

keys = list(result.keys())
keys.sort()

for i in keys:
    for j in result[i]:
        print(f"{i} {j}")