def solution(prices):
    N = len(prices)
    answer = [0]*N
    stack = []

    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = idx-j
        stack.append(idx)
    
    for i in stack:
        answer[i] = N-i-1
    
    return answer