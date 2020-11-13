mul = 1
lst = [0] * 10
for i in range(3):
    mul *= int(input())
for i in range(len(str(mul))):
    lst[int(str(mul)[i])] += 1
for i in range(10):
    print(lst[i])