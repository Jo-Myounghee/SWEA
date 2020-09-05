'''
abcd
3
P x
L
P y
'''
from sys import stdin
words = list(stdin.readline().rstrip('\n'))
N = int(stdin.readline().rstrip('\n'))
Given = [list(map(str, stdin.readline().rstrip('\n').split())) for _ in range(N)]
temp = []

keys = ['L', 'D', 'B', 'P']
for i in range(N):
    if Given[i][0] == keys[0]:
        if len(words) > 0:
            temp.append(words.pop())
    elif Given[i][0] == keys[1]:
        if len(temp) > 0:
            words.append(temp.pop())
    elif Given[i][0] == keys[2]:
        if len(words) > 0:
            words.pop()
    elif Given[i][0] == keys[3]:
        words.append(Given[i][1])

while len(temp) > 0:
    words.append(temp.pop())

print(''.join(words))

