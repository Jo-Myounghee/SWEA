from sys import stdin

N1, N2 = map(int, stdin.readline().split())

if N1 == N2:
    print(N1, N1, sep='\n')
else:
    if N1 > N2:
        Big, Sm = N1, N2
    else:
        Big, Sm = N2, N1
    for CF in range(Big, 0, -1):
        if N1 % CF == 0 and N2 % CF == 0:
            answer_CF = CF
            print(CF)
            break
    print((Big // answer_CF) * Sm)
