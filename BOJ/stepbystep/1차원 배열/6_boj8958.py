import sys
for _ in range(int(input())):
    score = list(sys.stdin.readline().rstrip())
    alpha = 1
    total = 0
    for i in range(len(score)):
        if score[i] == 'O':
            total += 1*alpha
            alpha += 1
        else:
            alpha = 1
    print(total)