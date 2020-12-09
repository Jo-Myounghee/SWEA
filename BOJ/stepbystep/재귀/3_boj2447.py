def star(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        first_row = [0] * (n//3)
        middle_row = [0] * (n//3)
        old_row = star(n//3)
        for i in range(n//3):
            first_row[i] = old_row[i]*3
            middle_row[i] = old_row[i] + ' '*(n//3) + old_row[i]
        return first_row + middle_row + first_row

answer = star(int(input()))
for i in range(0, len(answer), 3):
    print(answer[i], answer[i+1], answer[i+2], sep="\n")