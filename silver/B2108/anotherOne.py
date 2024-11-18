import sys

def slv():
    cases = int(sys.stdin.readline())

    user_list = []
    for _ in range(cases):
        user_list.append(int(sys.stdin.readline()))

    user_list.sort()

    m_freq = {}
    avg_sum = 0
    for i in user_list:
        avg_sum += i
        if i in m_freq:
            m_freq[i] += 1
        else :
            m_freq[i] = 1
            
    max_frequency = max(m_freq.values())
    max_frequency_nums = []
    for i in m_freq:
        if m_freq[i] == max_frequency :
            max_frequency_nums.append(i)
            
    if len(max_frequency_nums) > 1 :
        max_frequency_num = max_frequency_nums[1]
    else :
        max_frequency_num = max_frequency_nums[0]
        
    print(int(round(avg_sum / cases, 0)))
    print(user_list[int(cases/2)])
    print(max_frequency_num)
    print(user_list[-1] - user_list[0])

if __name__ == '__main__':
    slv()