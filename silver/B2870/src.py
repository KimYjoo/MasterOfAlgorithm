
T = int(input())
nums = []
for _ in range(T):
    a = input()
    bag = []
    for i in a:
        if i.isdigit():
            bag.append(i)
        else:
            if bag : nums.append(''.join(bag))
            bag.clear()
    if bag : nums.append(''.join(bag))

result = list(map(int, nums))
result.sort()

print('\n'.join(list(map(str,result))))