n = int(input())
cnt = 0
for i in range(1, n+1):
    if len(str(i)) <=2 :
        cnt += 1
    else:
        cnt_temp = 0
        for j in range(1, len(str(i))-1):
            if int(str(i)[j+1]) - int(str(i)[j]) == int(str(i)[j]) - int(str(i)[j-1]):
                cnt_temp += 1
            else:
                break
        if cnt_temp == len(str(i))-2:
            cnt += 1

print(cnt)