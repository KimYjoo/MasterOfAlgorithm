import sys

def slv():
    big_num, small_num = list(map(int, sys.stdin.readline().split()))

    if big_num < small_num:
        t = big_num
        big_num = small_num
        small_num = t
    
    denominator = 0
    divisor = int(big_num * small_num)

    while True:
        rest = big_num % small_num
        if rest == 0:
            denominator = small_num
            break
        big_num = small_num
        small_num = rest

    divisor = int(divisor / small_num)

    print(denominator)
    print(divisor)
        

if __name__ == "__main__":
    slv()