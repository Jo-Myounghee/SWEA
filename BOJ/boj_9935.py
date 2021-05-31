import sys

words = list(sys.stdin.readline().rstrip())
word = list(sys.stdin.readline().rstrip())
answer = []
for w in words:
    answer.append(w)
    if len(answer) >= len(word) and answer[len(answer) - len(word) : ] == word:
        for _ in range(len(word)):
            answer.pop()
print(*answer, sep="") if answer else print('FRULA')