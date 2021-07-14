def solution(brown, yellow):
    for m in range(3, brown):
        n = (brown // 2) + 2 - m
        if (n-2)*(m-2) == yellow:
            break
    return sorted([n, m], reverse=True)