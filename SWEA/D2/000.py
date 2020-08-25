T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dst = []
    for _ in range(N):
        dst_lst = list(map(int, input().split()))
        dst.append(dst_lst)

    result = [] #count를 담을 리스트
    for j in range(N):
        cnt = 0 # 한 행에 들어있는 숫자의 개수를 count하는 용도
        for i in range(N):
            Num = dst[i][j]
            if Num != 0:
                cnt += 1
            if Num == 0:
                result.append(cnt)
                cnt = 0

    lst = []    # count개수가 같은 것이 몇개인지 담을 리스트
    result_lst = list(range(1, N + 1)) # 열의 개수
    mul_lst = [] # 열

    for i in range(1, N + 1):
        mul = i * result.count(i)   # 행렬의 크기
        lst.append(result.count(i)) # 행의 크기
        mul_lst.append(mul)         # mul_lst => 행렬의 크기를 담은 리스트
    mul_result = [result_lst, lst, mul_lst] # mul_result = [열의 개수, 행의 개수, 행렬의 크기)

    for i in range(N):
        for j in range(N - 1, i, -1):
            if mul_result[2][j - 1] > mul_result[2][j]:     # mul_result에서 mul_lst
                for k in range(3):
                    mul_result[k][j - 1], mul_result[k][j] = mul_result[k][j], mul_result[k][j - 1]
    zero_num = mul_result[1].count(0)

    print(f'#{tc} {N - zero_num}', end=" ")
    for i in range(N):
        if mul_result[1][i] != 0:
            print(mul_result[0][i], mul_result[1][i], end=" ")
    print()