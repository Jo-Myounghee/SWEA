words = list(input())
alpha = list(range(65, 91))
answer = []
for word in words:
    answer.append(chr(alpha[ord(word)-68]))
print(*answer, sep='')