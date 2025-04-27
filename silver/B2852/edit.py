# 입력 : 
# 골이 들어간 횟수
# 득점 팀 , 득점 시간
import sys

def slv():
    goal_count = int(input())
    score_board = {'1':0, '2':0}
    lead_time_board = {'1':0, '2':0}
    END_TIME = '48:00'
    winning_team = ''
    start_time = '00:00'
    for _ in range(goal_count):
        team, goal_time = sys.stdin.readline().split()
        score_board[team] += 1
        if score_board['1'] == score_board['2']:
            lead_time_board[winning_team] += time_to_sec(goal_time) - time_to_sec(start_time)
            winning_team = ''
        else:
            if not winning_team:
                start_time = goal_time
                winning_team = team
    
    if winning_team:
        lead_time_board[winning_team] += time_to_sec(END_TIME) - time_to_sec(start_time)
    
    print(sec_to_time(lead_time_board['1']))
    print(sec_to_time(lead_time_board['2']))


def time_to_sec(goal_time):
    minute, second = map(int, goal_time.split(':'))
    return second + minute * 60
def sec_to_time(sec_time):
    minute = sec_time // 60 
    second = sec_time % 60
    return f'{minute:02}:{second:02}'


if __name__ == "__main__":
    slv()


    