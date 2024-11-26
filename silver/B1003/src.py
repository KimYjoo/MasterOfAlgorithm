import sys

def fibo(memo, count_memo, N):
    result = 0
    if N in memo:
        result = memo[N]
    else:
        result = fibo(memo, count_memo, N-1) + fibo(memo, count_memo, N-2)
        memo[N] = result
        count_memo[N] = (count_memo[N-1][0] + count_memo[N-2][0], count_memo[N-1][1] + count_memo[N-2][1])
    return result

if __name__ == "__main__":
    cases = int(sys.stdin.readline())
    memo = {1 : 1, 0 : 0}
    count_memo = {1 : (0, 1), 0 : (1, 0)}
    for _ in range(cases):
        N = int(sys.stdin.readline())
        fibo(memo, count_memo, N)
        print(f"{count_memo[N][0]} {count_memo[N][1]}")