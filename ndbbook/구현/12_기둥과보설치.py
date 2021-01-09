# https://programmers.co.kr/learn/courses/30/lessons/60061
'''
n = 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
'''
# 가능한 구조물인가
def is_possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        else:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            elif [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, stuff, operate in build_frame:
        if operate == 0:
            answer.remove([x, y, stuff])
            if not is_possible(answer):
                answer.append([x, y, stuff])
        else:
            answer.append([x, y, stuff])
            if not is_possible(answer):
                answer.remove([x, y, stuff])
    answer.sort()
    return answer

n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))
