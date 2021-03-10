def get_pi(words):
    lst_pi = [0] * len(words)
    j = 0
    for i in range(1, len(words)):
        while j > 0 and words[i] != words[j]:
            j = lst_pi[j-1]
        if words[i] == words[j]:
            lst_pi[i] = j+1
            j += 1
    return lst_pi

def KMP(input_words, pattern_words):
    pattern_pi = get_pi(pattern_words)
    j = 0
    cnt = 0
    idx_lst = []
    for i in range(len(input_words)):
        while j > 0 and input_words[i] != pattern_words[j]:
            j = pattern_pi[j-1]
        if input_words[i] == pattern_words[j]:
            if j == len(pattern_words) - 1:
                cnt += 1
                j = pattern_pi[j]
                idx_lst.append(i - len(pattern_words) + 2)
            else:
                j += 1
    return cnt, idx_lst

T = list(map(str, input()))
P = list(input())

cnt, idx_lst = KMP(T, P)
print(cnt)
print(*idx_lst)