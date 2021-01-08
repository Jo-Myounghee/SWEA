import sys
# sys.stdin = open('8input1.txt', 'r')
sys.stdin = open('8input2.txt', 'r')

inputs = input()
total = 0
words = []
for i in range(len(inputs)):
    try:
        total += int(inputs[i])
    except:
        words.append(inputs[i])
words.sort()
print(*words, total, sep='')