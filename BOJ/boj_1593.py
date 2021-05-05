'''
3 6
abc
abcbab
--> 2
'''
import sys

W, S = map(int, sys.stdin.readline().rstrip().split())
words = sys.stdin.readline().rstrip()
sentences = sys.stdin.readline().rstrip()
answer = 0

word_state = [0]*52
sentence_state = [0]*52
for word in words:
    if 'a' <= word <= 'z':
        word_state[ord(word)-ord('a')] += 1
    else:
        word_state[ord(word)-ord('A')+26] += 1

start, length = 0, 0

for _s in range(S):
    s = sentences[_s]
    if 'a' <= s <= 'z':
        sentence_state[ord(s)-ord('a')] += 1
    else:
        sentence_state[ord(s)-ord('A')+26] += 1
    length += 1

    if length == W:
        if word_state == sentence_state:
            answer += 1
        start_word = sentences[start]
        if 'a' <= start_word <= 'z':
            sentence_state[ord(start_word)-ord('a')] -= 1
        else:
            sentence_state[ord(start_word)-ord('A')+26] -= 1
        start += 1
        length -= 1

print(answer)