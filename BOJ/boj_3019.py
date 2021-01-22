C, P = map(int, input().split())
inputs = list(map(int, input().split()))
ans = 0
if P == 1:
    ans += C
    for i in range(C-3):
        if inputs[i] == inputs[i+1] == inputs[i+2] == inputs[i+3]:
            ans += 1

elif P == 2:
    for i in range(C-1):
        if inputs[i] == inputs[i+1]:
            ans += 1

elif P == 3:
    for i in range(C-1):
        if inputs[i] > 0 and inputs[i] == inputs[i+1] + 1:
            ans += 1
        elif i+2 < C and inputs[i] == inputs[i+1] and inputs[i+1] + 1 == inputs[i+2]:
            ans += 1

elif P == 4:
    for i in range(C-1):
        if inputs[i] + 1 == inputs[i+1]:
            ans += 1
        elif i+2 < C and inputs[i] > 0 and inputs[i] - 1 == inputs[i+1] and inputs[i+1] == inputs[i+2]:
            ans += 1

elif P == 5:
    for i in range(C-1):
        if inputs[i] + 1 == inputs[i+1]:
            ans += 1
        elif inputs[i] > 0 and inputs[i] - 1 == inputs[i+1]:
            ans += 1
        if i + 2 < C:
            if inputs[i] == inputs[i+1] == inputs[i+2]:
                ans += 1
            elif inputs[i] > 0 and inputs[i] == inputs[i+2] and inputs[i] - 1 == inputs[i+1]:
                ans += 1

elif P == 6:
    for i in range(C-1):
        if inputs[i] == inputs[i+1]:
            ans += 1
            if i+2 < C and inputs[i] == inputs[i+2]:
                ans += 1
        elif inputs[i] - 1 > 0 and inputs[i+1] == inputs[i] - 2:
            ans += 1
        elif i+2 < C and inputs[i] + 1 == inputs[i+1] and inputs[i+1] == inputs[i+2]:
            ans += 1

elif P == 7:
    for i in range(C-1):
        if inputs[i] == inputs[i+1]:
            ans += 1
            if i+2 < C and inputs[i] == inputs[i+2]:
                ans += 1
            elif i+2 < C and inputs[i] > 0 and inputs[i] - 1 == inputs[i+2]:
                ans += 1
        elif inputs[i] + 2 == inputs[i+1]:
            ans += 1

print(ans)
         
    # 5
    # for i in range(C):
    #     temp_cnt = 1
    #     prev = inputs[i]
    #     for j in range(i+1, C):
    #         if prev == inputs[j]:
    #             temp_cnt += 1
    #             if temp_cnt == 3:
    #                 ans += 1
    #                 break
    #         elif prev+1 == inputs[j]:
    #             ans += 1
    #             break
    #         elif j+2 < C and prev > 0 and inputs[j+1] == prev - 1 and inputs[j+2] == prev:
    #             ans += 1
    #         elif j+1 < C and prev > 0 and inputs[j+1] == prev - 1:
    #             ans += 1
                    
    # 3
    # for i in range(C):
    #     temp_cnt = 1
    #     prev = inputs[i]
    #     for j in range(i+1, C):
    #         if prev == inputs[j]:
    #             temp_cnt += 1
    #             if j+1 < C and prev > 0 and inputs[j+1] == prev-1:
    #                 ans += 1
    #                 break
    #             elif temp_cnt == 2 and j+1 < C and inputs[j+1] == prev + 1:
    #                 ans += 1
    #                 break