wrong_msg = "Goldbach's conjecture is wrong."
prime = [False, False] + [True] * 1000000

for i in range(2, 1000000):
    if prime[i]:
        for j in range(2*i, 1000000, i):
            prime[j] = False

while True:
    N = int(input())
    a, b = 0, 0
    if N == 0:
        break
    for i in range(N):
        if prime[i] and prime[N-i]:
            a, b = i, N-i
            break
    if a * b != 0:
        print(f'{N} = {a} + {b}')
    else:
        print(wrong_msg)

