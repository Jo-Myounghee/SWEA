def isPassword(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    v_cnt = 0
    for i in word:
        if i in vowels:
            v_cnt += 1
    c_cnt = len(word)-v_cnt
    if v_cnt < 1 or c_cnt < 2:
        return False
    return True

def func(s, cnt):
    global L, C, word, answer
    if cnt == L:
        if isPassword(word):
            answer.append(word)
        return
    
    for i in range(s, C):
        word += inputs[i]
        func(i+1, cnt+1)
        word = word[:-1]

L, C = map(int, input().split())
inputs = list(input().split())
inputs.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
consonant = []
word = ''
answer = []
func(0, 0)
print(*answer, sep="\n")