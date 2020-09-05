'''
8
4
3
6
8
7
5
2
1
'''
N = int(input())
given_lst = [int(input()) for _ in range(N)]
numbers = list(range(N, 0, -1))
stack = [0]
result = []
print_lst = []
flag = True
for i in range(N):
    if given_lst[i] != stack[-1]:
        if given_lst[i] > stack[-1]:
            while given_lst[i] != stack[-1]:
                stack.append(numbers.pop())
                print_lst.append('+')
        elif given_lst[i] < stack[-1]:
            print('NO')
            flag = False
            break
    if given_lst[i] == stack[-1]:
        result.append(stack.pop())
        print_lst.append('-')

if flag:
    for i in print_lst:
        print(i)

