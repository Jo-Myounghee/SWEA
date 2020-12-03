for tc in range(int(input())):
    n, words = input().split(" ")
    answer = ""
    for i in words:
        answer += i*int(n)
    print(answer)