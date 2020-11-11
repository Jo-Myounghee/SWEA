n = int(input())
origin = n
temp = n - 1
cnt = 0
while temp != origin:
    temp = (n % 10)*10 + ((n//10)+(n%10))%10
    cnt += 1
    n = temp
print(cnt)