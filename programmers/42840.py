def solution(answers):
    sol = []
    scores = []
    students = [[1, 2, 3, 4, 5], 
                [2, 1, 2, 3, 2, 4, 2, 5], 
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
               ]
    for j in range(3):
        student = students[j]
        cnt = 0
        for i in range(len(answers)):
            answer = answers[i]
            if answer == student[i%len(student)]:
                cnt += 1
        scores.append(cnt)
    for i in range(3):
        if scores[i] == max(scores):
            sol.append(i+1)
    return sol