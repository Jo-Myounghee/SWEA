import sys
for tc in range(1, int(input())+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(tc, a, b, a+b))