def solution(priorities, location):
    answer = 0
    n = 0
    N = len(priorities)
    visited = [False] * N
    max_lst = priorities[:]
    while True:
        if priorities[n] == max(max_lst):
            answer += 1
            if n == location:
                return answer
            visited[n] = True
            max_lst.pop(max_lst.index(priorities[n]))
        n = (n+1)%N
    return answer