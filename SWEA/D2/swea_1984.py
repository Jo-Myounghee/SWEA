import sys

sys.stdin = open("./input_data/input_1984.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, T = map(int, input().split())
    scores = []
    number = 0
    result = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for n in range(N):
        number += 1
        score = list(map(int, input().split()))
        avg_score = float((score[0]*0.35) + (score[1]*0.45) + (score[2]*0.2))
        score.append(avg_score)
        score.append(number)
        scores.append(score)
    for _ in range(N):
        for i in range(N):
            if i > 0:
                if scores[i][3] > scores[i-1][3]:
                    tmp = scores[i]
                    scores[i] = scores[i-1]
                    scores[i-1] = tmp
    for n in range(N):
        if scores[n][4] == T:
            for i in range(1, 10):
                if n >= (N*0.1*(10-i)):
                    print(f'#{tc} {result[10-i]}')
                    break
