a, b, c = map(int, input().split())
# a + bx < cx
# x > a / (c - b)
if b == c:
    print(-1)
    exit()
    
x = a / (c - b)
# print(x)
if x < 0:
    print(-1)
else:
    import math
    print(math.floor(x) + 1)