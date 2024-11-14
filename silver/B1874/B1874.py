import sys
# def slv(progress) :
#     A = [i for i in range(1,max(progress)+1)]
#     B = [1 for i in range(1,max(progress)+1)]
#     C = []
#     ret = []
#     for i in progress :
#         for j in range(1, i + 1) :
#             if B[j-1] == 1 :
#                 C.append(j)
#                 ret.append('+')
#                 B[j-1] = 2
#         if C.pop() != i : 
#             return False, ret
#         else :
#             ret.append('-')

#     return True, ret
#시간 초과

def slv(progress) :
    A = []
    ret = []
    [A.append(i+1) for i in range(len(progress))]
    
    now = -1
    save = 0
    max_len = len(progress)
    for i in progress :
        if(now > i-1):
            if i < max_len and A[i-1] != A[i] :
                print('NO')
                return
        else :
            for _ in range(i - save) :
                ret.append('+')
            save = i
        A[i - 1] -= 1
        now = i - 1
        ret.append('-')
    [print(i)for i in ret]
    
        
if __name__ == "__main__" :
    N = int(input())

    progress = [int(sys.stdin.readline().strip()) for _ in range(N)]
    
    ans = slv(progress)