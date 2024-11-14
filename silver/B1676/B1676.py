N = int(input())

# ret = 1
# for i in range(1, N + 1) :
#     ret *= i

# ret = str(ret)

# arr = list(ret)
# arr1 = arr[::-1]

# idx = 0
# for i in arr1 :
#     if(i != "0") : break
#     idx += 1
# print(idx)

cnt = 0
n = N
while n != 0 :
    n //= 5
    cnt += n
print(cnt)

print(N//5 + N//25 + N//125)