import sys; sys.stdin = open('3input.txt', 'r')

# S의 길이가 100만보다 작기 때문에 O(N)가능

def all_zero(n):
    cnt = 0
    pre_one = False
    for i in range(len(n)):
        if not pre_one and n[i] == '1':
            pre_one = True
            cnt += 1
        elif n[i] == '0':
            pre_one = False
    return cnt

def all_one(n):
    cnt = 0
    pre_zero = False
    for i in range(len(n)):
        if not pre_zero and n[i] == '0':
            pre_zero = True
            cnt += 1
        elif n[i] == '1':
            pre_zero = False
    return cnt

num = input()

cnt_zero = all_zero(num)
cnt_one = all_one(num)

if cnt_zero > cnt_one:
    print(cnt_one)
else:
    print(cnt_zero)

