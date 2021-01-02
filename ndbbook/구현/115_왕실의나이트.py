# input : a1
# output : 2

now_x, now_y = input()
now_x = ord(now_x) - ord('a')
now_y = int(now_y) - 1
answer = 0
diag = [[2, 1], [1, 2], [2, -1], [-2, 1], [-1, 2], [1, -2], [-2, -1], [-1, -2]]

for i in range(len(diag)):
    test_x = now_x + diag[i][0]
    test_y = now_y + diag[i][1]
    if 0 <= test_x < 8 and 0 <= test_y < 8:
        answer += 1

print(answer)