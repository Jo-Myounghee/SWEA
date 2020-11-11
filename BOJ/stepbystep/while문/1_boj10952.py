import sys
a = b = 1
while a and b:
    a, b = map(int, sys.stdin.readline().split())
    if a + b == 0:
        break
    print(a+b)