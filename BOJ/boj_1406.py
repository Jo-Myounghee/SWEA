'''
abcd
3
P x
L
P y
'''
from sys import stdin
text = list(stdin.readline().rstrip('\n'))
N = int(stdin.readline().rstrip('\n'))
cnt = 0
temp = []
for command in stdin:
    if command[0] == 'L' and text:
        temp.append(text.pop())
    elif command[0] == 'R' and temp:
        text.append(temp.pop())
    elif command[0] == 'B' and text:
        text.pop()
    elif command[0] == 'P':
        text.append(command[2])
    cnt += 1
    if cnt == N:
        break

print(''.join(text+temp[::-1]))

