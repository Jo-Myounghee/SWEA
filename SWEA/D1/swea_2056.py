T = int(input())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T+1):
    datetime = str(input())
    year = datetime[0:4]
    mon = datetime[4:6]
    day = datetime[6:8]
    if int(mon) == 0 or int(mon) > 12:
        result = -1
    elif int(day) == 0 or int(day) > month[int(mon)-1]:
        result = -1
    else:
        result = f'{year}/{mon}/{day}'

    print(f'#{tc} {result}')