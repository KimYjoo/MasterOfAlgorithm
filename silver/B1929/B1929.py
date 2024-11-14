def slv(minimum, maximum):
    prime_numbers = []
    rslt_prime_numbers = []
    for i in range(2, minimum) :
        check_prime_number(i, prime_numbers)
    for i in range(minimum, maximum + 1):
        get_rslt_prime_number(i, prime_numbers, rslt_prime_numbers)
    result = '\n'.join(rslt_prime_numbers)
    print(result)

def check_prime_number(number, prime_numbers) :
    for i in prime_numbers :
        if number % i == 0 :
            return
    prime_numbers.append(number)
    return

def get_rslt_prime_number(number, prime_numbers, rslt_prime_numbers) :
    for i in prime_numbers :
        if number % i == 0 :
            return
    prime_numbers.append(number)
    rslt_prime_numbers.append(str(number))
    return

if __name__ == "__main__":
    M, N = map(int, input().split())
    slv(M,N)