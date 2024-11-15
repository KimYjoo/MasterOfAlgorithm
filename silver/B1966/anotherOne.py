import sys
from collections import deque

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    input_length, find_index = map(int, sys.stdin.readline().split())
    user_input = deque(list(map(int, sys.stdin.readline().split())))
    user_input_index = deque(list(range(input_length)))
    count = 1
    max_num = max(user_input)
    
    while True :
        candidate = user_input.popleft()
        candidate_index = user_input_index.popleft()
        
        if candidate == max_num: 
            if candidate_index == find_index : 
                print(count)
                break
            max_num = max(user_input)
            count += 1
            continue
        
        user_input.append(candidate)
        user_input_index.append(candidate_index)
