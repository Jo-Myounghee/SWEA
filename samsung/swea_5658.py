'''
1
12 10
1B3B3B81F75E

5
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
20 14
88F611AE414A751A767B
24 16
044D3EBA6A647B2567A91D0E
28 11
8E0B7DD258D4122317E3ADBFEA99
'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(input())
    words = []
    word_len = N//4
    for i in range(N):
        for j in range(0, N, word_len):
            word = ''.join(lst[j:j+word_len])
            word_to_num = int(word, 16)
            if word_to_num not in words:
                words.append(word_to_num)
        a = lst.pop()
        lst.insert(0, a)
    print('#{} {}'.format(tc, sorted(words, reverse=True)[K-1]))