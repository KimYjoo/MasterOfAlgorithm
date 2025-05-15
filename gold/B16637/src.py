def slv():
    n = int(input().strip())
    expr = input().strip()
    result = get_max_result(expr, n, 2, int(expr[0]))
    print(result)

def get_max_result(expr, n, index, sum):
        if index >= n:
            return sum
        
        # 바로 계산
        result = get_max_result(expr, n, index + 2, calculator(sum, expr[index], expr[index - 1]))

        # 괄호 생성
        if index + 2 < n:
            temp = calculator(expr[index], expr[index + 2], expr[index + 1])
            result2 = get_max_result(expr, n, index + 4, calculator(sum, temp, expr[index - 1]))
            result = max(result, result2)
        
        return result

def calculator(num1, num2, op):
    num1 = int(num1)
    num2 = int(num2)
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    
if __name__ == "__main__":
    slv()