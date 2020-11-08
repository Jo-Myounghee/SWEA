N = int(input())

# DP 테이블 초기화
d = [0] * 30001 # N은 1부터 30,000까지 가능 -> 30001개의 리스트 생성

# DP 보텀업 (2부터 시작 ~ N까지)
for i in range(2, N+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[N])