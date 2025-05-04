t = int(input().strip())
stairs = []
memo = [[] for _ in range(t)]
for _ in range(t):
    stairs.append(int(input().strip()))

memo[0].append(0)
memo[1].append(1)
for idx in range(2, t):
    sum = 0
    print(idx)
    print(memo[idx-1])
    if memo[idx-1]:
        if not idx-2 in memo[idx-1]:
            for i in memo[idx-1]:
                sum += stairs[i]

    sum1 = 0
    for i in memo[idx-2]:
        sum1 += stairs[i]
    
    memo[idx] = max(sum, sum1)

sum1 = 0
for i in memo[t-1]:
    sum1 += stairs[i]

print(sum1)