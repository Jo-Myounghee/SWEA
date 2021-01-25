from itertools import combinations, permutations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
nums = range(N)

min_val = 1e9
for i in range(1, N//2+1):
    team1 = list(combinations(nums, i))
    for j in range(len(team1)):
        team2 = [list(range(N)) for _ in range(len(team1))]
        for k in range(len(team1[j])):
            team2[j].remove(team1[j][k])
        for j in range(len(team1)):
            temp_team1_sum = 0
            temp_team2_sum = 0
            if len(team1[j]) > 1:
                temp_team1 = list(combinations(team1[j], 2))
                for k in range(len(temp_team1)//2):
                    temp_team1_sum += board[temp_team1[k][0]][temp_team1[k][1]]
                    temp_team1_sum += board[temp_team1[k][1]][temp_team1[k][0]]
            if len(team2[j]) > 1:
                temp_team2 = list(combinations(team2[j], 2))
                for k in range(len(temp_team2)//2):
                    temp_team2_sum += board[temp_team2[k][0]][temp_team2[k][1]]
                    temp_team2_sum += board[temp_team2[k][1]][temp_team2[k][0]]
            
            temp_min = abs(temp_team1_sum-temp_team2_sum)
            if temp_min < min_val:
                min_val = temp_min

print(min_val)