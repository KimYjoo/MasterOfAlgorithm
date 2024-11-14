def slv(M, N) :
    for num in range(M, N+1):
        if num == 1 : continue
        checkPrimeNum(num)

def checkPrimeNum(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 :
            return
    print(num)

if __name__ == "__main__" :
    M, N = map(int, input().split())
    slv(M, N)