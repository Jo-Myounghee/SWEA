def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        day = (100-progress)//speed
        if (100-progress)%speed:
            day += 1
        days.append(day)
    cnt = 0
    max_val = days[0]
    while days:
        now = days.pop(0)
        if now <= max_val:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max_val = now
    answer.append(cnt)
    return answer