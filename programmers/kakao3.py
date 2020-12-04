def solution(words, queries):
    answer = [0] * len(queries)
    for i in range(len(queries)):
        same_visited = []
        no_same_visited = []
        cnt = 0
        for j in words:
            if len(queries[i]) != len(j):
                continue
            else:
                k = 0
                if queries[i] == '?'*len(queries[i]):
                    cnt += 1

                elif j in same_visited:
                    cnt += 1

                elif j in no_same_visited:
                    continue

                elif queries[i][k] == '?':
                    temp_word = queries[i][::-1]
                    k = len(j) - temp_word.index('?')
                    if queries[i][k:] == j[k:]:
                        cnt += 1
                        same_visited.append(j)
                        continue
                    no_same_visited.append(j)
                else:
                    k = queries[i].index('?')
                    if queries[i][:k] == j[:k]:
                        cnt += 1
                        same_visited.append(j)
                        continue
                    no_same_visited.append(j)
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