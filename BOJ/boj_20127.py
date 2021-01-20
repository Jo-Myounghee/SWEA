def is_up(numbers):
    for i in range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            return False
    return True

def is_down(numbers):
    for i in range(1, len(numbers)):
        if numbers[i-1] < numbers[i]:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))

no_answer = True

if N == 2:
    print(1)
    no_answer = False
elif N == 1:
    print(0)
    no_answer = False
else:
    for i in range(N):
        temp_numbers = numbers[i:] + numbers[:i]
        if is_up(temp_numbers):
            print(i)
            no_answer = False
            break
        if is_down(temp_numbers):
            print(i)
            no_answer = False
            break

if no_answer:
    print(-1)