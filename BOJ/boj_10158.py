w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

newX = (p + t) % (2*w)
newY = (q + t) % (2*h)

X = (2*w) - newX if newX > w else newX
Y = (2*h) - newY if newY > h else newY

print(X, Y)
