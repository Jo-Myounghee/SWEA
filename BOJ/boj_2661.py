def solution(n):
    global answer, temp

    def is_available(t):
        _left, _right = len(t)-1, len(t)-1
        cnt = 0
        while _left >= 0:
            _left -= 1
            cnt += 1
            if t[_left] == t[_right]:
                if t[_left-cnt+1:_left+1] == t[_right-cnt+1:_right+1]:
                    return False
        return True

    if n == N:
        _temp = int(''.join(map(str, temp)))
        answer = min(answer, _temp)
        print(answer)
        exit()

    if temp:
        for i in range(1, 4):
            if temp[-1] != i:
                temp.append(i)
                if is_available(temp):
                    solution(n+1)
                temp.pop()
    else:
        temp.append(1)
        solution(n+1)


answer = 10**80
temp = []
N = int(input())
solution(0)
print(answer)