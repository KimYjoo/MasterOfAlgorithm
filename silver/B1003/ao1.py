import sys
cases = int(sys.stdin.readline())
case_list = [int(sys.stdin.readline()) for _ in range(cases)]
case_max = max(case_list)

fibo = [[0, 0] for _ in range(case_max + 1)]
fibo[0] = [1, 0]
if case_max > 0: 
    fibo[1] = [0, 1]
for i in range(2, case_max + 1):
    fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]
    
for i in case_list:
    print(f"{fibo[i][0]} {fibo[i][1]}")
