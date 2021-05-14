def solution(n, lost, reserve):
    answer = n
    losts = [l for l in lost if l not in reserve]
    reserves = [r for r in reserve if r not in lost]
        
    for i in range(n+2):
        if i in losts:
            if i-1 in reserves:
                reserves.pop(reserves.index(i-1))
            elif i+1 in reserves:
                reserves.pop(reserves.index(i+1))
            else:
                answer -= 1
    return answer