# def is_up(numbers):
#     for i in range(1, len(numbers)):
#         if numbers[i-1] > numbers[i]:
#             return False
#     return True

# def is_down(numbers):
#     for i in range(1, len(numbers)):
#         if numbers[i-1] < numbers[i]:
#             return False
#     return True

N = int(input())
numbers = list(map(int, input().split()))

first_up_cut = 0
first_down_cut = 0
up_cut = 0
down_cut = 0
up_ans = False
down_ans = False
for i in range(1, len(numbers)):
    if numbers[i-1] > numbers[i]:
        up_cut += 1
        first_up_cut = i
    if up_cut > 1:
        break

if up_cut == 1:
    temp_lst = numbers[i:] + numbers[:i]
    for i in range(1, len(temp_lst)):
        if temp_lst[i-1] > temp_lst[i]:
            print(-1)
            break


for i in range(1, len(numbers)):
    if numbers[i-1] > numbers[i]:
        down_cut += 1
        first_down_cut = i
    if down_cut > 1:
        break

if down_cut == 1:
    temp_lst = numbers[i:] + numbers[:i]
    for i in range(1, len(temp_lst)):
        if temp_lst[i-1] < temp_lst[i]:
            print(-1)
            break

if down_cut == 0 and up_cut == 0:
    print(0)

print(first_down_cut)


# first = numbers[0]
# prev = numbers[0]
# state = ''
# cnt = 0
# flag = '11'
# for i in range(1, len(numbers)):
#     if prev < numbers[i]:
#         if state and state != 'up':
#             cnt += 1
#             first = numbers[i]
#         state = 'up'
#     elif prev > numbers[i]:
#         if state and state != 'down':
#             cnt += 1
#             first = numbers[i]
#         state = 'down'

#     if cnt > 1:
#         print(-1)
#         break

# if cnt == 0:
#     print(0)
# elif cnt == 1:
#     flag = '0'
#     lst = numbers[numbers.index(first):] + numbers[:numbers.index(first)]
#     if first < numbers[numbers.index(first)+1]:
#         for i in range(1, len(numbers)):
#             if lst[i-1] > lst[i]:
#                 print(-1)
#                 flag = '1'
#                 break
#     else:
#         now = 'down'
#         for i in range(1, len(numbers)):
#             if lst[i-1] < lst[i]:
#                 print(-1)
#                 flag = '1'
#                 break  
# if flag and flag == '0':
#     print(numbers.index(first))
    
    

