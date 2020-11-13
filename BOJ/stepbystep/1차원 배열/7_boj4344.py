import sys
for _ in range(int(input())):
    scores = list(map(int, sys.stdin.readline().split()))
    num = scores.pop(0)
    avg = sum(scores) // num
    cnt = 0
    for score in scores:
        if score > avg:
           cnt += 1
    print('%0.3f'%round((cnt/num)*100, 3), '%', sep="")
