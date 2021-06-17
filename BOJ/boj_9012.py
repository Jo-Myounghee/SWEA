def is_valid(lst):
    stack = []
    for i in lst:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                print('NO')
                return
    if stack:
        print('NO')
        return
    print('YES')


N = int(input())
for _ in range(N):
    is_valid(input())