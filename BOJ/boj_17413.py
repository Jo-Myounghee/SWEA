words = input()
temp = []
result = []
flag = False
for i in range(len(words)):
    if words[i] == '<':
        while temp:
            result.append(temp.pop(-1))
        flag = True
        temp.append(words[i])
    elif words[i] == '>':
        temp.append(words[i])
        flag = False
        while temp:
            result.append(temp.pop(0))
    elif words[i] == ' ':
        if flag:
            temp.append(words[i])
        else:
            while temp:
                result.append(temp.pop(-1))
            result.append(' ')
    else:
        temp.append(str(words[i]))
while temp:
    result.append(temp.pop(-1))
print(''.join(result))

