def solution(s):
    s = s[2:len(s)-2]
    answer = []
    inputs = list(s.split('},{'))
    for i in range(len(inputs)):
        inputs[i] = list(inputs[i].split(','))
    inputs.sort(key=lambda x:len(x))
    answer.append(int(inputs[0][0]))
    for i in range(len(inputs)-1):
        prev_lst = inputs[i]
        next_lst = inputs[i+1]
        num = [x for x in next_lst if x not in prev_lst]
        answer.append(int(num[0]))
    return answer