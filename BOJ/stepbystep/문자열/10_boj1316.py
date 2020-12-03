cnt = 0
for i in range(int(input())):
    alp = [False]*26
    flag = False
    words = input()
    for j in range(len(words)):
        if alp[ord(words[j])-ord('a')]:
            if words[j - 1] == words[j]:
                continue
            else:
                flag = True
                break
        else:
            alp[ord(words[j])-ord('a')] = True
    if not flag:
        cnt += 1
print(cnt)