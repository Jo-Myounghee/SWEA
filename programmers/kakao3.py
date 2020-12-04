def solution(words, queries):
    answer = []
    for i in queries:
        cnt = 0
        for j in words:
            if len(i) != len(j):
                continue
            else:
                k = 0
                if i == '?'*len(i):
                    cnt += 1

                elif i[k] == '?':
                    temp_word = i[::-1]
                    k = len(j) - temp_word.index('?')
                    if i[k:] == j[k:]:
                        cnt += 1
                else:
                    k = i.index('?')
                    if i[:k] == j[:k]:
                        cnt += 1
        answer.append(cnt)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

# 시간 엄청 줄인 코드

# a = str(11123456)
# a = a[::-1]
# inx = str(a).index('1')
# print(inx)
# a = a[::-1]
# print(a[len(a)-inx-1])