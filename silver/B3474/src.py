T = int(input())

for _ in range(T):
    num = int(input())
    five_square = 5
    result = 0
    while five_square <= num:
        result += num // five_square
        five_square *= 5 
    
    print(result)