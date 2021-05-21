def solution(s):
    answer = True
    s = list(s)
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    if p == 0 and y == 0:
        return True
    if y == p:
        return True
    return False