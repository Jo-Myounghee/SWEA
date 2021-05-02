def comb(cnt, start):
    global pair
    if cnt == 2:
        if sum(heights) - sum(pair) == 100:
            for i in heights:
                if i != pair[0] and i != pair[1]:
                    print(i)
            exit()
        return
    for i in range(start, 9):
        pair.append(heights[i])
        comb(cnt+1, i+1)
        pair.pop()

heights = [int(input()) for _ in range(9)]
heights.sort()
pair = []
comb(0, 0)