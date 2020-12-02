alpha=[-1]*26

words = str(input())
for i in range(len(words)):
    order = ord(words[i])-ord('a')
    if alpha[order] == -1:
        alpha[order] = i
    else:
        continue

print(*alpha)