import sys; sys.stdin = open('4input.txt', 'r')

def sum_lst(ans, k):
    if k == N:
        if not ans in sum_list:
            sum_list.append(ans)
        return
    else:
        sum_lst(ans+money[k], k+1)
        sum_lst(ans, k+1)

N = int(input())
money = list(map(int, input().split()))
sum_list = []
sum_lst(0, 0)
sum_list.sort()
for i in range(sum_list[-1]):
    if i != sum_list[i]:
        print(i)
        break

