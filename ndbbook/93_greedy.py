# 큰 수의 법칙
'''
M 이 10,000 이하이므로 해결 가능
만약 M의 크기가 100억 이상으로 커진다면 시간 초과 판정 날 것
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

while 1:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)