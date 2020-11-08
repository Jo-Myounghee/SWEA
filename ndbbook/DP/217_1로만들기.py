'''
input
26
output
3
'''
def cal(n):
    global cnt
    if n == 1:
        return cnt
    elif n % 5 == 0:
        cnt += 1
        cal(cal(n//5))
    elif n % 3 == 0:
        cnt += 1
        cal(cal(n//3))
    elif n % 2 == 0:
        cnt += 1
        cal(cal(n//2))
    else:
        cal(cal(n-1))

N = int(input())
cnt = 0

print(cal(N))




