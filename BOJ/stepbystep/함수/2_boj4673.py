lst = [False] * 10000

def self_num(n):
    total = 0
    for i in range(len(str(n))):
        total += int(str(n)[i])
    total += n
    if total >= 10000:
        return
    if lst[total-1]:
        return
    lst[total-1] = True
    return self_num(total)

for i in range(10000):
    if not lst[i]:
        self_num(i+1)

for i in range(len(lst)-1):
    if not lst[i]:
        print(i+1)