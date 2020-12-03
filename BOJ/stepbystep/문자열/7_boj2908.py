a, b = input().split()
a = ''.join(reversed(a))
b = ''.join(reversed(b))
print(a) if int(a) > int(b) else print(b)