# https://www.acmicpc.net/problem/18406

import sys
# sys.stdin = open('7input.txt', 'r')
sys.stdin = open('7input1.txt', 'r')

numbers = list(map(int, input()))
N = len(numbers)
left_sum = sum(numbers[:N//2])
right_sum = sum(numbers[N//2:N])
print('LUCKY') if left_sum == right_sum else print('READY')


