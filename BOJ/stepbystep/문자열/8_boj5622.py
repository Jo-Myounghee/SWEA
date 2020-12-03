# print(8+6+8+2+4+2+6)

# answer = 0
# for i in input():
#     num = ord(i)-ord('A')
#     if num > 21:
#         answer += 10
#     else:
#         if num == 18:
#             answer += 8
#         elif num == 21:
#             answer += 9
#         else:
#             answer += ((num // 3) + 3)
#
# print(answer)

for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     print(min(ord(c)-64, 25)*28//89)
    temp = min(ord(c)-64, 25)*28//89
    print(temp, end=" ")
print()
# answer = 0
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     print(min(ord(c)-64, 25)*28//89)
    temp = min(ord(c)-64, 25)*5//16
    print(temp, end=" ")
print()
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     print(min(ord(c)-64, 25)*28//89)
    temp = min(ord(c)-64, 25)*5
    print(temp, end=" ")

#     answer += temp
    # print(temp)
# print(answer)

# print(ord('A'))

# print(sum(min(ord(c)-64,25)*28//89+3for c in input()))