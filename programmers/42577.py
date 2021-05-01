def solution(phone_book):
    answer = True
    hash = {}
    for phone in phone_book:
        hash[phone] = 1
    for phone in phone_book:
        temp = ""
        for num in phone:
            temp += num
            if temp in hash and temp != phone:
                answer = False
                break
    return answer