# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    if len(s) == 1:
        return 1
    answer = '0'* 1000
    # print(s)
    for word_len in range(1, len(s)//2+1):
        # print('단위', word_len)
        prev = s[:word_len]
        cnt = 1
        temp_word = ''
        for j in range(word_len, len(s)+word_len, word_len):
            now = s[j:j+word_len]
            if prev == now:
                cnt += 1
            elif prev != now and cnt > 1:
                temp_word += (str(cnt)+prev)
                cnt = 1
                prev = now
            else:
                temp_word += prev
                prev = now
        if cnt > 1:
            temp_word += (str(cnt)+prev)
        print(temp_word)
        if len(temp_word) < len(answer):
            answer = temp_word
    return len(answer)

# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))