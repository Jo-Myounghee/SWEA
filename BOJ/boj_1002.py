T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif dist == 0 and r1 != r2:
        print(0)
    elif dist < abs(r1 - r2):
        print(0)
    elif dist > abs(r1+r2):
        print(0)
    elif dist == abs(r1 - r2):
        print(1)
    elif dist == abs(r1 + r2):
        print(1)
    elif abs(r1-r2) < dist < abs(r1 + r2):
        print(2)