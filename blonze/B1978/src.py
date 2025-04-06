import sys

def slv():
    N = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))

    max_num = max(nums)
    number_plate = [True] * (max_num+1)
    number_plate[0] = False
    number_plate[1] = False

    for num in range(2, nums):
        if not number_plate[num]:
            continue
        per = 2
        while num * per <= max_num:
            number_plate[num * per] = False
            per += 1
    
    result = 0
    for i in nums:
        if number_plate[i]:
            result += 1
    print(result)
    
if __name__ == "__main__":
    slv()

## 개선 버전


import sys

def get_prime_sieve(max_val):
    is_prime = [False, False] + [True] * (max_val - 1)
    for i in range(2, int(max_val ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_val + 1, i):
                is_prime[j] = False
    return is_prime

def solve():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    sieve = get_prime_sieve(max(nums))
    print(sum(1 for num in nums if sieve[num]))

if __name__ == "__main__":
    solve()
