N, M = map(int, input().split())

people = list(range(1, N+1))
print(people)
temp = []
result = []
while len(result) < N:
    i = 1
    t = 1
    while len(result) < N:
        t = ((i * M) % N) - 1
        if people[t]:
            result.append(people[t])
            people[t] = 0
        i += 1
        if i * M > N:
            while 0 in people:
                del people[people.index(0)]


print(result)