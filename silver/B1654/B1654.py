import sys

K, N = map(int, input().split())
data = [int(sys.stdin.readline().strip()) for i in range(K)]

left = 1
right = max(data)

while(left <= right) :
    
    mid = (right + left)//2
    ret = 0
    for i in data :
         ret += i // mid
    if ret >= N :
        left = mid + 1
    else : 
        right = mid - 1

print(right)
