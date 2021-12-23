a, b, v = map(int, input().split())
# a * day - b * (day - 1) > v
# day > (v - b) / (a - b)
day = (v - b) / (a - b)
# print(day)
import math
print(math.ceil(day))