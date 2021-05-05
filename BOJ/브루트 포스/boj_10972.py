def next():
    for i in range(len(numbers)-1, 0, -1):
        prev = numbers[i-1]
        now = numbers[i]
        if prev < now:
            for j in range(len(numbers)-1, i-1, -1):
                if numbers[j] > prev:
                    numbers[j], numbers[i-1] = numbers[i-1], numbers[j]
                    return i

N = int(input())
numbers = list(map(int, input().split()))

if numbers == sorted(numbers, key=lambda x:-x):
    print(-1)
else:
    i = next()
    sort_numbers = sorted(numbers[i:])
    print(*numbers[:i], *sort_numbers, sep=" ")