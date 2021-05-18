def solution(array, commands):
    answer = []
    for command in commands:
        _s, _e, _a = command[0], command[1], command[2]
        ans = sorted(array[_s-1:_e])
        answer.append(ans[_a-1])
    return answer