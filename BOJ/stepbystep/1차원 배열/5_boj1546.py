import sys
int(input())
lst = list(map(int, sys.stdin.readline().split()))
answer = ((sum(lst) / len(lst))/max(lst))*100
print(answer)