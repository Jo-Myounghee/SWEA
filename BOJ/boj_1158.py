def game(s):
    global arr

    answer = []
    if not answer:
        now = s-1
        a = arr.pop(now)
        answer.append(a)
    while arr:
        now = (now + K - 1) % len(arr)
        a = arr.pop(now)
        answer.append(a)
    return f"<{', '.join(map(str, answer))}>"


N, K = map(int, input().split())
arr = list(range(1, N+1))
print(game(K))