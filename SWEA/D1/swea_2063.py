n = int(input())

numbers = list(map(int, input().split()))

for i in range(n):
    for j in range(1, n):
        if numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]

print(numbers[n//2])