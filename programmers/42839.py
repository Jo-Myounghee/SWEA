import itertools, math

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(words):
    answer = 0
    visited = []
    for i in range(1, len(words)+1):
        nums = list(map(''.join, itertools.permutations(words, i)))
        for num in nums:
            num = int(num)
            if num not in visited:
                visited.append(num)
                if is_prime(num):
                    answer += 1
    return answer