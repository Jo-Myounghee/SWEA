'''
6 60
5
1 2 30
2 5 70
5 6 60
3 4 40
1 6 40

4 40
3
1 4 40
2 3 40
3 4 40
'''
N, C = map(int, input().split())
M = int(input())
items = [[] for _ in range(N)]
inputs = [list(map(int, input().split())) for _ in range(M)]
inputs.sort(key=lambda inputs: (inputs[1], inputs[0]))
sends = [0] * (N+1)

ans = 0
for i in range(len(inputs)):
    s, g, val = inputs[i]
    max = 0
    isBig = False
    for k in range(s, g):
        # 애초에 넘겨져 있다면
        if sends[k] >= C:
            isBig = True
        # 만약 넘기면
        if sends[k] < C and sends[k] + val >= C and sends[k] + val - C > max:
            # 넘긴 값
            max = sends[k] + val - C
    # 넘긴게 없었다면
    if not isBig and max == 0:
        for k in range(s, g):
            sends[k] += val
        ans += val

    # 넘긴게 있었다면
    elif not isBig and max:
        for k in range(s, g):
            sends[k] += (val - max)
        ans += (val - max)

print(ans)
