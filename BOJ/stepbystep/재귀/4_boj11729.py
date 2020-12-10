# 옮길 원반이 현재 있는 출발점 기둥 from_pos
# 원반을 옮길 도착점 기둥 to_pos
# 옮기는 과정에서 사용할 보조 기둥 aux_pos

def hanoi(n, from_pos, to_pos, aux_pos):
    global cnt, answer
    if n == 1:
        cnt += 1
        answer.append(f'{from_pos} {to_pos}')
        return

    hanoi(n-1, from_pos, aux_pos, to_pos)
    answer.append(f'{from_pos} {to_pos}')
    cnt += 1
    hanoi(n-1, aux_pos, to_pos, from_pos)

cnt = 0
answer = []
hanoi(int(input()), 1, 3, 2)
print(cnt)
for i in range(len(answer)):
    print(answer[i])
    # 원반 n-1개를 aux_pos로 이동 (출발점 from_pos, 도착점 aux_pos, 보조 기둥 to_pos)
    # 가장 큰 원반을 목적지로 이동
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(출발점 aux_pos, 목적지 to_pos, 보조기둥 from_pos)
