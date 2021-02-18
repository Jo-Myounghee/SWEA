from itertools import permutations

# 순열로 팀짜기
#
# def perm(idx, n, k):
#     global temp, A
#     # print(n)
#     if n == k:
#         B = [0]*len(A)
#         for i in range(len(A)):
#             B[i] = A[i]
#         if not B in temp[idx]:
#             temp[idx].append(B)
#
#     else:
#         for i in range(n, k):
#             A[n], A[i] = A[i], A[n]
#             perm(idx, n+1, k)
#             A[n], A[i] = A[i], A[n]
#     return


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

temp = [[] for _ in range(N)]
for i in range(len(board)):
    A = board[i][:3]+board[i][4:]

    tmp = list(set(permutations(A)))
    # 현재 최고 점수, 멈춘 idx
    now_score, now_idx = 0, 0
    for j in range(len(tmp)):
        tmp[j] = [board[i][3]] + list(tmp[j])





# now = [] # 여기에 (획득 점수, 멈춘 idx) 담기
# now_lst = [[] for _ in range(N)]
# now_score = 0 # 획득 점수
# max_score = 0 # 현재 가장 높은 점수
# for i in range(len(temp)):
#     for j in range(len(temp[i])):
#         temp[i][j] = [board[i][3]] + temp[i][j]
#         out = 0
#         for k in range(9):
#             if out == 3 and now_score > max_score:
#
#             if temp[i][j][k] == 0:
#                 out += 1
        # print(temp[i][j])