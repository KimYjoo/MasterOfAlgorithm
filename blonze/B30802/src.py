# 펜은 참가자 수와 일치 P장 묶음이나 한개씩
# 티셔츠는 이상이어야함 같은사이즈 T장 묶음으로 주문 가능

import sys 

def slv():
    N = int(sys.stdin.readline().strip())
    sizes_list = map(int, sys.stdin.readline().split())
    T, P = map(int, sys.stdin.readline().split())

    shirt_number = 0
    for size_index in sizes_list:
        if size_index > 0:
            if size_index > T:
                shirt_number += size_index // T
                if size_index % T > 0:
                    shirt_number += 1
            else:
                shirt_number += 1

    print(shirt_number)
    print(int(N // P), N % P)


if __name__ == "__main__":
    slv()