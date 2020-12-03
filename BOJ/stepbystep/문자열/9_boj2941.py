cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = input()
cnt = len(words)

for i in range(len(cro)):
    cnt -= (len(cro[i])-1) * words.count(cro[i])

if words.count('dz=') and words.count('z='):
    cnt += 1 * words.count('dz=')

print(cnt)
