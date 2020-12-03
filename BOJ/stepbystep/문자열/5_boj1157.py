alpha = [0] * 26
for i in input().upper():
    alpha[ord(i)-ord('A')] += 1

print('?') if alpha.count(max(alpha)) > 1 else print(chr(alpha.index(max(alpha))+ord('A')))