def solution(clothes):
    answer = 1
    hash = {}
    for val, key in clothes:
        if key in hash.keys():
            hash[key].append(val)
        else:
            hash[key] = [val]
    for val in hash.values():
        answer *= (len(val)+1)
    answer -= 1
    return answer