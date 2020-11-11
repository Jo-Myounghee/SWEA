hour = range(0, 24)

h, m = map(int, input().split())
if m - 45 < 0:
    answer_min = m + 15
    answer_hour = h - 1
    if answer_hour < 0:
        answer_hour = hour[answer_hour]
else:
    answer_min = m - 45
    answer_hour = h

print(answer_hour, answer_min, sep=" ")