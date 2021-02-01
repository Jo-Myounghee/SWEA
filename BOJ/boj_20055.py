N, K = map(int, input().split())
boxes = list(map(int, input().split()))
print(boxes)
robots = [0] * N
cnt = 0

while True:
    cnt += 1
    print(cnt)
    # 1. 회전
    print(robots)
    print('######시작#######')
    boxes = [boxes[-1]] + list(boxes[0:len(boxes)-1])
    robots = [robots[-1]] + list(robots[0:len(robots)-1])
    # 1-1. 만약 robot의 N번째 인덱스에 로봇이 존재하면 -> 로봇 제거
    if robots[-1] == 1:
        robots[-1] = 0
    print(boxes, 'boxes')
    print(robots, 'robots')

    # 2. 로봇 이동
    for i in range(len(robots)-1, -1, -1):
        if robots[i]:
            if i+1 < N-1 and boxes[i+1] > 0 and robots[i+1] != 1:
                robots[i] = 0
                robots[i+1] = 1
                boxes[i+1] -= 1
            elif i+1 == N-1 and boxes[i+1] > 0:
                boxes[i+1] -= 1
                robots[i] = 0
    print(boxes, 'boxes')
    print(robots, 'robots')


    # 3. 로봇 올림
    if robots[0] == 0 and boxes[0] > 0:
        robots[0] = 1
        boxes[0] -= 1
    print(boxes, 'boxes')
    print(robots, 'robots')


    # 4. 내구성이 0인 개수가 K이상이면 끝
    if boxes.count(0) >= K:
        print(cnt)
        break
    print('#-------------')