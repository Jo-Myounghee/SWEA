N = int(input())

for _ in range(N):
    inputs = list(map(int, input().split()))
    num = inputs.pop(0)
    l = list(set(inputs))
    cnt = 0
    answer = False
    for i in range(len(l)):
        if inputs.count(l[i]) > num//2:
            print(l[i])
            answer = True
            break
        cnt += inputs.count(l[i])
        if cnt > num//2:
            answer = True
            print('SYJKGW')
            break

    if not answer:
        print('SYJKGW')