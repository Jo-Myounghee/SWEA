MIN, MAX = map(int, input().split())
check = [0] * 1000001

for i in range(2, MAX):
    n = i**2
    if n > MAX:
        break

    start = n - (MIN % n)

    if start == n:
        start = 0

    for j in range(start, MAX-MIN+1, n):
        check[j] = 1

print(check[:MAX-MIN+1].count(0))