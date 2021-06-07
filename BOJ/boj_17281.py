def play():
    cur = 0
    inning = 0
    out = 0
    score = 0
    lu1, lu2, lu3 = 0, 0, 0

    while True:
        player = data[inning][order[cur] - 1]
        if player == 0:
            out += 1
            if out == 3:
                out = 0
                inning += 1
                lu1 = lu2 = lu3 = 0
                if inning == N:
                    return score
        elif player == 1:
            if lu3:
                score += 1
                lu3 = 0
            if lu2:
                lu3, lu2 = 1, 0
            if lu1:
                lu2, lu1 = 1, 0
            lu1 = 1

        elif player == 2:
            if lu3:
                score += 1
                lu3 = 0
            if lu2:
                score += 1
                lu2 = 0
            if lu1:
                lu3, lu1 = 1, 0
            lu2 = 1

        elif player == 3:
            if lu3:
                score += 1
                lu3 = 0
            if lu2:
                score += 1
                lu2 = 0
            if lu1:
                score += 1
                lu1 = 0
            lu3 = 1

        else:
            score += (lu1 + lu2 + lu3 + 1)
            lu1 = lu2 = lu3 = 0

        cur = (cur + 1) % 9


def perm(cnt, num):
    global answer
    if cnt == 8:
        answer = max(answer, play())
        return

    for i in range(9):
        if order[i]:
            continue
        order[i] = num
        perm(cnt + 1, num + 1)
        order[i] = 0


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

order = [0] * 9
order[3] = 1
answer = 0

perm(0, 2)
print(answer)