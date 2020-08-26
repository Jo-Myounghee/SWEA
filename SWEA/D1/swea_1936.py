a, b = map(int, input().split())

if a == 1 and b == 3:
    print('A')
elif a == 3 and b == 1:
    print('B')
elif a < b:
    print('B')
else:
    print('A')