import sys
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

for _ in range(int(input())):
    N1, N2 = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(int(N1 * N2 / gcd(N1, N2))) + "\n")
