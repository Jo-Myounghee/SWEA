def solution(words, queries):
    answer = []
    for i in queries:
        cnt = 0
        for j in words:
            no_same = False
            if len(i) != len(j):
                continue
            else:
                for k in range(len(i)):
                    if i[k] == '?':
                        continue
                    elif i[k] != '?' and i[k] != j[k]:
                        no_same = True
                        break
                if not no_same:
                    cnt += 1
        answer.append(cnt)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))