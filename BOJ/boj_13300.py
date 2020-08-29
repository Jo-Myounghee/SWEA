n, k = map(int, input().split())

info = [list(map(int, input().split())) for i in range(n)]

boy = [0, 0, 0, 0, 0, 0]
girl = [0, 0, 0, 0, 0, 0]

for i in range(n):
    if info[i][0]:
        boy[info[i][1]-1] += 1
    else:
        girl[info[i][1]-1] += 1

room = 0
for i in range(6):
    if boy[i] > k:
        if boy[i] % k == 0:
            room += boy[i] // k
        else:
            room += ((boy[i] // k) + 1)
    elif boy[i] == 0:
        pass
    else:
        room += 1

    if girl[i] > k:
        if girl[i] % k == 0:
            room += girl[i] // k
        else:
            room += ((girl[i] // k) + 1)
    elif girl[i] == 0:
        pass
    else:
        room += 1

print(room)

