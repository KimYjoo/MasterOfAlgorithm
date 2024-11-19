from collections import deque


def slv():
    N = int(input())
    arr = deque(range(1, N + 1))
    if N == 1 :
        print(1)
        return
    if N % 2 != 0 :
        arr = pre_cut_odd(arr)
    print(cut_odd(arr))

def pre_cut_odd(arr):
    # 초기 홀수번째 인덱스 삭제
    new_arr = deque([arr[i] for i in range(len(arr)) if i % 2 != 0])
    # 첫 번째 값을 맨 뒤로 이동
    new_arr.append(new_arr.popleft())
    return new_arr

def cut_odd(arr):
    while len(arr) > 1:
        # 짝수번째 요소만 남기기
        arr = deque([arr[i] for i in range(len(arr)) if i % 2 != 0])
    return arr[0]

if __name__ == "__main__":
    slv()