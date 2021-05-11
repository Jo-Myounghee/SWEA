'''
7 1 2 3 4 5 6 7
0
'''
def find(start, cnt):
    global answer, nums, n
    if cnt == 6:
        print(*answer, sep=" ")
        return
    for i in range(start, n):
        answer.append(nums[i])
        find(i+1, cnt+1)
        answer.pop()

while True:
    inputs = list(map(int, input().split()))
    if inputs == [0]:
        break
    else:
        n, nums = inputs[0], inputs[1:]
        answer = []
        find(0, 0)
    print()