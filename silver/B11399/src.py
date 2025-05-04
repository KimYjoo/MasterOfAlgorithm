n = int(input().strip())
drawout = list(map(int, input().split()))
drawout.sort()

result = 0
sum = 0
for i in drawout:
    result += sum + i
    sum += i

print(result)