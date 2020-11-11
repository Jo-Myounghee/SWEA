import sys
a = b = 1
while a and b:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break