def solution(words, queries):
    answer = []
    for i in queries:
        cnt = 0
        for j in words:
            no_same = False
            if len(i) != len(j):
                continue
            else:
                k = 0
                # 효율성 테케3이 ?????인 글자인듯
                if i == '?'*len(i):
                    cnt += 1
                elif i[k] == '?':
                    while i[k] == '?':
                        k += 1
                    if i[k:] == j[k:]:
                        cnt += 1
                else:
                    while i[k] != '?':
                        k += 1
                    if i[:k] == j[:k]:
                        cnt += 1
        answer.append(cnt)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))