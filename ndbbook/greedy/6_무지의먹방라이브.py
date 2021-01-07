# 처음 접근 방법 - 정확성 100, 효율성 0 (출력 크기 초과, cus: k의 범위가 2*10^13까지 존재)
# swea의 피자 만들기 문제 같음 (피자 오븐에 넣는 문제, 원형 큐 사용)
def solution(food_times, k):
    answer = 0
    temp_lst = list(range(len(food_times)))
    print(temp_lst)
    while temp_lst:
        answer += 1
        if answer == k+1:
            return temp_lst[0] + 1
        food_times[temp_lst[0]] -= 1
        if food_times[temp_lst[0]]:
            temp_lst.append(temp_lst[0])
        temp_lst.pop(0)
    return -1

# k의 범위가 크기 때문에 수학 문제로 접근

def solution(food_times, k):
    answer = 0
    N = len(food_times)
    if N > k:
        return k + 1
    else:
        div = k // N
        some = k % N
        new_lst = [food_times[i] - (div + 1) for i in range(N)]
        cor = 0
        for i in range(N):
            if new_lst[i] < 0:
                cor -= new_lst[i]
        if cor > 0:
            answer = ((some + cor) % N)
            cnt = 0
            while new_lst[answer] < 0:
                cnt += 1
                answer += 1
                if cnt == N:
                    return -1
            return answer + 1
        else:
            return (some % N) + 1

    return answer

# 첫번째 원형큐 + 두번째의 수학적 접근
def solution(food_times, k):
    answer = 0
    N = len(food_times)
    div = k // N
    some = k % N
    new_lst = [(food_times[i] - div) for i in range(N)]
    id_lst = [i for i in range(N) if new_lst[i] > 0]
    # print(id_lst)
    # return
    cnt = 0
    while len(id_lst) >= 0:
        print(id_lst)
        cnt += 1
        if cnt == some+1:
            return id_lst[0] + 1
        new_lst[id_lst[0]] -= 1
        if new_lst[id_lst[0]]:
            id_lst.append(id_lst[0])
        id_lst.pop(0)
    # if new_lst[some] > 0:
    #     return some
    # else:
    #     while new_lst[(some%N)] <= 0:
    #         some += 1
    return -1

# 세번째 정리본
def solution(food_times, k):
    answer = 0
    N = len(food_times)
    div = k // N
    some = k % N
    new_lst = [(food_times[i] - div) for i in range(N)]
    id_lst = [i for i in range(N) if new_lst[i] > 0]
    cnt = 0
    while len(id_lst) >= 0:
        print(id_lst)
        cnt += 1
        if cnt == some+1:
            return id_lst[0] + 1
        new_lst[id_lst[0]] -= 1
        if new_lst[id_lst[0]]:
            id_lst.append(id_lst[0])
        id_lst.pop(0)
    return -1

# 며칠동안 고민했는데 접근이 잘못되었다. 다시 풀어보자.