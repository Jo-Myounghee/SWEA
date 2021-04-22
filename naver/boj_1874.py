N = int(input())
inputs = [int(input()) for _ in range(N)]
numbers = list(range(N, 0, -1))
stack = [0]
result = []
print_lst = []
flag = True

for i in range(N):
    if inputs[i] != stack[-1]:
        if inputs[i] > stack[-1]:
            while inputs[i] != stack[-1]:
                stack.append(numbers.pop())
                print_lst.append('+')
        elif inputs[i] < stack[-1]:
            print('NO')
            flag = False
            break
    if inputs[i] == stack[-1]:
        result.append(stack.pop())
        print_lst.append('-')

if flag:
    print(*print_lst, sep="\n")