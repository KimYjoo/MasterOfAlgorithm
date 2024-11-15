import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    input_length, find_index = map(int, sys.stdin.readline().split())
    user_input = list(map(int, sys.stdin.readline().split()))
    count = 1
    now_value = 9
    user_input_tmp = user_input[:]
    
    while now_value != 0 :
        if not now_value in user_input_tmp:
            now_value -= 1
            continue
        now_max_index = user_input_tmp.index(now_value)
        forward = user_input_tmp[:now_max_index]
        backward = user_input_tmp[now_max_index + 1:]
        user_input_tmp = backward + forward
        
        if find_index == now_max_index :
            print(count)
            break
        elif find_index > now_max_index : 
            find_index -= len(forward) + 1
        elif find_index < now_max_index :
            find_index += len(backward)
        count += 1