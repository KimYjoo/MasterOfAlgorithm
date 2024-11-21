cases = int(input())
arr = [list(map(int,input().split())) for i in range(cases)]

arr.sort(key=lambda x : (x[0], x[1]))

for x, y in arr :
    print(x, y)