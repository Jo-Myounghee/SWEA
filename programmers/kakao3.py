def solution(words, queries):
    answer = [0] * len(queries)
    visited = []
    for i in range(len(queries)):
        if queries[i] in visited:
            cnt = answer[visited.index(queries[i])]
            answer[i] = cnt
            visited.append(queries[i])
            continue

        cnt = 0
        for j in words:
            if len(queries[i]) != len(j):
                continue
            else:
                if queries[i] == '?'*len(queries[i]):
                    cnt += 1

                elif queries[i][0] == '?':
                    temp_word = queries[i][::-1]
                    k = len(j) - temp_word.index('?')
                    if queries[i][k:] == j[k:]:
                        cnt += 1

                else:
                    k = queries[i].index('?')
                    if queries[i][:k] == j[:k]:
                        cnt += 1
        visited.append(queries[i])

        answer[i] = cnt
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

# 시간 엄청 줄인 코드

# a = str(11123456)
# a = a[::-1]
# inx = str(a).index('1')
# print(inx)
# a = a[::-1]
# print(a[len(a)-inx-1])