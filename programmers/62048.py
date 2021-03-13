import math

def solution(w,h):
    if w == 1 or h == 1:
        return 0
    now = 0
    gcm = math.gcd(w, h)
    if gcm != 1: # 서로소가 아닌 경우
        cnt = max(w, h)//gcm
        for i in range(1, (w//gcm)):
            now_val = (h / w) * i
            if now != int(now_val):
                now = int(now_val)
                if now_val - now:
                    cnt += 1
        cnt *= gcm
    else:
        cnt = max(w, h)
        for i in range(1, w+1):
            now_val = (h / w) * i
            if now != int(now_val):
                now = int(now_val)
                if now_val - now:
                    cnt += 1
            
    answer = (w*h)-cnt
    return answer