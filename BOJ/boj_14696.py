T = int(input())

for tc in range(1, T+1):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    del a[0]
    del b[0]
    flag = False
    for i in range(1, 5)[::-1]:
        if a.count(i) > b.count(i):
            print('A')
            flag = True
            break
        elif a.count(i) < b.count(i):
            print('B')
            flag = True
            break
        else:
            continue
    if flag == False:
        print('D')
