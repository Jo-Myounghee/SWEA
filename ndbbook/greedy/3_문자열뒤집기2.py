# import sys; sys.stdin = open('3input.txt', 'r')

num = input()
cnt = 0
prev = '2'
for i in range(len(num)):
    if prev != num[i]:
        cnt += 1
        prev = num[i]

print(cnt//2)
