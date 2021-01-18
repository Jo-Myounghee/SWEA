N = int(input())
words = [input() for _ in range(N)]

pattern_lst = []
cnt = 0
for i in range(N):
    word = words[i]
    temp_pattern = []
    prev = 'a'
    temp_pattern.append(prev)
    for j in range(1, len(word)):
        if word[j] in word[:j]:
            idx = word.index(word[j])
            temp_pattern.append(temp_pattern[idx])
        else:
            prev = chr(ord(prev)+1)
            temp_pattern.append(prev)
    pattern_lst.append(temp_pattern)

pattern_lst.sort()

for i in range(N):
    for j in range(N):
        if i != j and pattern_lst[i] == pattern_lst[j]:
            cnt += 1

print(cnt//2)