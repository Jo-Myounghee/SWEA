# 1. boj1712

> https://www.acmicpc.net/problem/1712

```python
A, B, C = map(int, input().split())
print(-1) if (C-B) <= 0 or A//(C-B) < 0 else print(A//(C-B)+1)
```

- `if (C-B) <= 0 or A//(C-B) < 0`에서 `A//(C-B)`를 먼저 쓰면 런타임 에러가 뜸

  -> (C-B) == 0인 경우에는 zero에러가 뜨기 때문

  그래서 (C-B) <= 0 먼저 써줘야함