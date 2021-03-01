lst = list(map(int, input().split()))

a = list(range(1, 9))
d = list(range(8, 0, -1))

if lst == a:
    print('ascending')
elif lst == d:
    print('descending')
else:
    print('mixed')