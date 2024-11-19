N = int(input())

# N보다 작은 가장 큰 2의 거듭제곱 찾기
power_of_two = 1
while power_of_two * 2 <= N:
    power_of_two *= 2

# 결과 출력: 2의 거듭제곱이면 그대로 출력, 그렇지 않으면 계산
print(N if power_of_two == N else (N - power_of_two) * 2)