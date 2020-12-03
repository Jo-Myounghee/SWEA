A, B, C = map(int, input().split())
print(-1) if (C-B) <= 0 or A//(C-B) < 0 else print(A//(C-B)+1)
