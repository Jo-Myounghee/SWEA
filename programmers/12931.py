def solution(n):
    words = str(n)
    answer = 0
    for i in words:
        answer += int(i)
    return answer