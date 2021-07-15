def solution(number, k):
    answer = 0
    temp = ''

    def make_num(n, cnt, s):
        nonlocal temp, answer
        if cnt == n:
            answer = max(int(temp), answer)
            return
        for i in range(s, len(number)):
            temp += number[i]
            make_num(n, cnt + 1, i + 1)
            temp = temp[:-1]

    make_num(len(number) - k, 0, 0)
    return str(answer)