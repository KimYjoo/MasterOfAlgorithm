import sys



def slv():
    cases = int(sys.stdin.readline())

    user_list = []
    for _ in range(cases):
        user_list.append(int(sys.stdin.readline()))

    user_list.sort()

    average = get_average(user_list, cases)
    middle_num = get_middle_num(user_list, cases)
    most_frequency = get_most_frequency(user_list)
    range_degree = get_range(user_list)
    print(f'{average}')
    print(f'{middle_num}')
    print(f'{most_frequency}')
    print(f'{range_degree}')
    
def get_average(user_list, cases):
    sum = 0
    for i in user_list :
        sum += i
    return int(round(sum / cases, 0))

def get_middle_num(user_list, cases):
    return user_list[int(cases/2)]

def get_most_frequency(user_list):
    most_frequency = 0
    mf_num = [user_list[0]]
    now_num = user_list[0]
    count_frequency = 0

    for i in range(len(user_list)):
        if now_num != user_list[i]:
            if most_frequency < count_frequency:
                most_frequency = count_frequency
                mf_num = [now_num]
            elif most_frequency == count_frequency:
                mf_num.append(now_num)
            now_num = user_list[i]
            count_frequency = 1
            continue
        count_frequency += 1

    if most_frequency < count_frequency:
        most_frequency = count_frequency
        mf_num = [now_num]
    elif most_frequency == count_frequency:
        mf_num.append(now_num)
    
    if len(mf_num) > 1 :
        return mf_num[1]
    return mf_num[0]

def get_range(user_list):
    return user_list[-1] - user_list[0]

if __name__ == '__main__':
    slv()