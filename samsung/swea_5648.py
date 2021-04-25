'''
1
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
'''
dir = ((0, 1), (0, -1), (-1, 0), (1, 0))
T = int(input())
for tc in range(1, T+1):
    ans = 0
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(2001):
        temp = []
        for i in range(len(info)):
            nx, ny, nd, nk = info[i]
            tx, ty = nx + dir[nd][0], ny + dir[nd][1]
            temp.append([tx, ty, nd, nk])

        temp.sort(key=lambda x: (x[0], x[1]))
        # [x, y]
        same = []
        same_k_sum = 0
        if temp:
            prev = temp[-1]
            temp_info = [temp[i][:] for i in range(len(temp))]
            for i in range(len(temp)-2, -1, -1):
                if [temp[i][0], temp[i][1]] not in same and (prev[0], prev[1]) == (temp[i][0], temp[i][1]):
                    same.append([temp[i][0], temp[i][1]])
                    same_k_sum += prev[3]
                    same_k_sum += temp[i][3]
                    prev = temp[i]
                    temp_info.pop(i+1)
                    temp_info.pop(i)
                elif [temp[i][0], temp[i][1]] in same and (prev[0], prev[1]) == (temp[i][0], temp[i][1]):
                    same_k_sum += temp[i][3]
                    temp_info.pop(i)
                else:
                    prev = temp[i]
            ans += same_k_sum
            info = temp_info
        else:
            break
    print('#{} {}'.format(tc, ans))
