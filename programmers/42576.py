def solution(participant, completion):
    hash=dict()
    for part in participant:
        if part in hash:
            hash[part] += 1
        else:
            hash[part] = 1
    for name in completion:
        if hash[name] == 1:
            del hash[name]
        else:
            hash[name] -= 1
    answer = list(hash.keys())[0]
    return answer