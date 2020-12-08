def factorial(n, answer):
    if n == 1:
        return answer
    elif n == 0:
        return 0
    else:
        answer *= n
        return factorial(n-1, answer)

print(factorial(int(input()), 1))