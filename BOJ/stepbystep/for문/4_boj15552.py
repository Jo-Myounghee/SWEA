'''
input
5
1 1
12 34
5 500
40 60
1000 1000
'''
import sys
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a+b)