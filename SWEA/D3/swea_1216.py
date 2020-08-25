import sys

sys.stdin = open("./input/input_1216.txt", "r")

def pal(text):
    for m in range(100, 0, -1):
        for i in range(100-m+1):
            if text[i] == text[i+m-1]:
                words_tmp = text[i:i+m]
                flag = True
                for j in range(m//2):
                    if words_tmp[j] != words_tmp[-j-1]:
                        flag = False
                        break
                if flag == True:
                    return m

for _ in range(10):
    tc = input()
    arr = []
    total = 0
    
    for _ in range(100):
        row = input()
        arr.append(row)
        if total < pal(row):
            total = pal(row)
                                        
    for i in range(100):
        words_col = ''
        for j in range(100):
            words_col += arr[j][i]
        if total < pal(words_col):
            total = pal(words_col)
    print(f'#{tc} {total}')