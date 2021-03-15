def solution(record):
    answer = []
    temp_answer = [record[i].split(" ") for i in range(len(record))]
    id_name = dict()
    for i in range(len(record)):
        if temp_answer[i][0] != 'Leave':
            id_name[temp_answer[i][1]] = temp_answer[i][2]
    for i in range(len(record)):
        if temp_answer[i][0] == 'Enter':
            answer.append(f"{id_name[temp_answer[i][1]]}님이 들어왔습니다.")
        elif temp_answer[i][0] == 'Leave':
            answer.append(f"{id_name[temp_answer[i][1]]}님이 나갔습니다.")
    return answer