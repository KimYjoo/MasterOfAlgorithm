# 입력 : 
# 골이 들어간 횟수
# 득점 팀 , 득점 시간
import sys

def slv():
    goal_count = int(input())
    goal_stack = []
    goal_board = {'1': '00:00', '2':'00:00'}
    for _ in range(goal_count):
        team, goal_time = sys.stdin.readline().split()
        goal_stack.append((team, goal_time))
    winning_team = ''
    start_time = ''
    goal_differ = 0
    for team, goal_time in goal_stack:
        if goal_differ == 0 and winning_team == '':
            winning_team = team
            start_time = goal_time
            goal_differ = 1
        else:
            if winning_team != team:
                goal_differ -= 1
            else:
                goal_differ += 1
            if goal_differ == 0:
                goal_board[winning_team] = time_save(start_time, goal_time, goal_board[winning_team])
                winning_team = ''
    if goal_differ > 0:
        goal_board[winning_team] = time_save(start_time, '48:00', goal_board[winning_team])
    print(goal_board['1'])
    print(goal_board['2'])


def time_save(start_time, end_time, saved_time):
    start_minnute, start_second = map(int, start_time.split(':'))
    end_minnute, end_second = map(int, end_time.split(':'))
    saved_minnute, saved_second = map(int, saved_time.split(':'))

    minnute_temp = end_minnute - start_minnute
    second_temp = end_second - start_second
    if second_temp < 0:
        minnute_temp += 1
        second_temp += 60
    minnute_temp += saved_minnute
    second_temp += saved_second
    minnute_temp = str(minnute_temp)
    second_temp = str(second_temp)
    if len(minnute_temp) < 2:
        minnute_temp = '0' + minnute_temp
    if len(second_temp) < 2:
        second_temp = '0' + second_temp
    return minnute_temp + ':' + second_temp

if __name__ == "__main__":
    slv()


    