a = input()
b = input()
for i in range(len(b)-1, -1, -1):
    print(int(a)*int(b[i]))
print(int(a)*int(b))