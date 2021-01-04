import sys; sys.stdin = open('1input.txt', 'r')

N = int(input())
people = list(map(int, input().split()))

people.sort()

temp_cnt = 0
cnt = 0
for person in people:
    temp_cnt += 1
    if temp_cnt >= person:
        cnt += 1
        temp_cnt = 0
print(cnt)